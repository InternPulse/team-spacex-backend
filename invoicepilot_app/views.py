# invoicepilot_app/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile, Invoice, PaymentTransaction, InvoiceItem, ClientContact, Notification, RecurringInvoiceSchedule
from .serializers import ProfileSerializer, InvoiceSerializer, OurUserCreateSerializer, PaymentTransactionSerializer, InvoiceItemSerializer, ClientContactSerializer, NotificationSerializer, RecurringInvoiceScheduleSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class SignUp(generics.CreateAPIView):
    serializer_class = OurUserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class MyAccount(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class Login(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)

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