# invoices/views.py
from django.utils import timezone
from django.http import FileResponse
from io import BytesIO
from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer,SendInvoiceEmailSerializer, InvoiceEmptySerializer
from utils.mailer import send_email_with_pdf
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from reportlab.pdfgen import canvas
from rest_framework import serializers
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import NotFound
from .permissions import IsVerifiedPermission
class InvoiceItemListView(generics.ListAPIView):
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated, IsVerifiedPermission]

    def get_queryset(self):
        invoice_id = self.kwargs.get('invoice_id')
        return InvoiceItem.objects.filter(invoice_id=invoice_id)

class AddInvoiceItemView(generics.CreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated, IsVerifiedPermission]

    def create(self, request, *args, **kwargs):
        invoice_id = kwargs.get('invoice_id')
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
        except Invoice.DoesNotExist:
            return Response({'detail': 'Invoice not found.'}, status=404)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(invoice=invoice)
        return Response(serializer.data, status=201)




class SendInvoiceEmailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsVerifiedPermission]
    serializer_class = SendInvoiceEmailSerializer
    parser_classes = [FileUploadParser]

    def post(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise NotFound(detail='Invoice not found.')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject = "Invoice Notification"
        pdf_content = serializer.data.get('pdf_content')

        # Call the function to send the email
        success = send_email_with_pdf(subject, pdf_content, invoice)

        if success:
            return Response({'detail': 'Email sent successfully.'})
        else:
            return Response({'detail': 'Failed to send email.'}, status=500)


class GenerateInvoicePDFView(generics.GenericAPIView):
    queryset = InvoiceItem.objects.all()
    permission_classes = [IsAuthenticated, IsVerifiedPermission]

    def get(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({'detail': 'Invoice not found.'}, status=404)

        # Get all invoice items associated with the invoice
        invoice_items = invoice.items.all()

        # Create a PDF buffer
        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer)
        
        # Write invoice details
        title = invoice.title
        pdf.drawString(100, 800, f'Title: {title}')
        # Add other invoice details here

        # Write invoice items details
        y_position = 780  # Initial y-position for the first item
        for invoice_item in invoice_items:
            pdf.drawString(100, y_position, f'Description: {invoice_item.description}')
            pdf.drawString(100, y_position - 20, f'Quantity: {invoice_item.quantity}')
            pdf.drawString(100, y_position - 40, f'Unit Price: ${invoice_item.unit_price}')
            pdf.drawString(100, y_position - 60, f'Tax: ${invoice_item.tax}')
            pdf.drawString(100, y_position - 80, f'Subtotal: ${invoice_item.subtotal}')
            pdf.drawString(100, y_position - 100, f'Total: ${invoice_item.total}')
            y_position -= 120  # Adjust y-position for the next item

        pdf.save()
        pdf_buffer.seek(0)

        filename = f'invoice_{invoice.id}.pdf'
        pdf_content = pdf_buffer.getvalue()

        response = FileResponse(pdf_buffer, as_attachment=True, filename=filename)
        return response


class InvoiceListView(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsVerifiedPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, sender=self.request.user)

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsVerifiedPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, sender=self.request.user)
