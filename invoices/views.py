# invoices/views.py
from django.shortcuts import render
from django.utils import timezone
from django.http import FileResponse
from io import BytesIO
from typing import Optional  # Add this import for Optional
from .models import Invoice
from .utils import send_email_with_pdf
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Invoice, InvoiceItem, MailRecord
from .serializers import NewCustomerSerializer, InvoiceSerializer, InvoiceItemSerializer
from .models import InvoiceItem as AppInvoiceItem  # Update the import based on your app name

from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas

class SendInvoiceEmailView(APIView):
    def post(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
            subject = request.data.get('subject', 'Invoice')
            message = request.data.get('message', 'Please find the attached invoice.')
            pdf_content = request.data.get('pdf_content')  # You may need to handle file upload here
            
            # Call the function to send the email
            success = send_email_with_pdf(subject, message, pdf_content, invoice)
            
            if success:
                return Response({'detail': 'Email sent successfully.'})
            else:
                return Response({'detail': 'Failed to send email.'}, status=500)
        except Invoice.DoesNotExist:
            return Response({'detail': 'Invoice not found.'}, status=404)



class GenerateInvoicePDFView(APIView):
    def get(self, request, pk):
        invoice_item = InvoiceItem.objects.get(pk=pk)
        invoice_item.invoice_date_generated = timezone.now()
        invoice_item.save()

        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer)
        pdf.drawString(100, 800, f'Customer Name: {invoice_item.owner.username}')
        pdf.drawString(100, 780, f'Description: {invoice_item.description}')
        pdf.drawString(100, 760, f'Quantity: {invoice_item.quantity}')
        pdf.drawString(100, 740, f'Price: ${invoice_item.price}')
        pdf.drawString(100, 720, f'Date Created: {invoice_item.date_created}')
        pdf.drawString(100, 700, f'Date Generated: {invoice_item.invoice_date_generated}')
        pdf.save()
        pdf_buffer.seek(0)

        filename = f'{invoice_item.owner.username}_{invoice_item.description}.pdf'
        response = FileResponse(pdf_buffer, as_attachment=True, filename=filename)
        return response

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = NewCustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, sender=self.request.user)

class InvoiceItemCreateView(generics.CreateAPIView):
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        invoice_id = self.kwargs['invoice_id']
        invoice = Invoice.objects.get(pk=invoice_id)
        serializer.save(invoice=invoice)

def send_email_with_pdf(subject: str, message: str, pdf_content: bytes, invoice: Invoice, template: Optional[str] = 'default') -> bool:
    """Send an email containing the invoice to the customer"""
    email = EmailMessage(
        subject,
        message,
        'your-email@example.com',
        to=[invoice.recipient.email],
    )

    if pdf_content:
        email.attach('invoice.pdf', pdf_content, 'application/pdf')
    sent = email.send()
    if sent:
        MailRecord.objects.create(
            invoice=invoice,
            to=invoice.recipient.email,
            template_used=template
        )
        return True
    return False