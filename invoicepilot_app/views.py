# invoicepilot_app/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Invoice, PaymentTransaction, InvoiceItem, ClientContact, Notification, RecurringInvoiceSchedule
from .serializers import InvoiceSerializer, OurUserCreateSerializer, PaymentTransactionSerializer, InvoiceItemSerializer, ClientContactSerializer, NotificationSerializer, RecurringInvoiceScheduleSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DashboardAPIView(generics.RetrieveAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.filter(user=request.user).order_by('-date_created')[:5]
        serializer = self.get_serializer(invoices, many=True)
        return Response(serializer.data)

class PaymentTransactionListCreateView(generics.ListCreateAPIView):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InvoiceItemListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClientContactListCreateView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecurringInvoiceScheduleListCreateView(generics.ListCreateAPIView):
    queryset = RecurringInvoiceSchedule.objects.all()
    serializer_class = RecurringInvoiceScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TestMailerView(generics.RetrieveAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        from invoicepilot_app.mailer import Invoice, send_email_with_pdf
        iv = Invoice.objects.get(id=1)
        sent = send_email_with_pdf('Invoice', 'Here is the summary of your order', b'pdf content', iv)
        return Response({'message': 'Mail sent'} if sent else {'message': 'Mail not sent'})