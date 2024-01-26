# invoices/views.py
from django.utils import timezone
from django.http import FileResponse
from io import BytesIO
from typing import Optional  # Add this import for Optional
from .models import Invoice, InvoiceItem, MailRecord
from .serializers import InvoiceSerializer, InvoiceItemSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from rest_framework.generics import ListCreateAPIView

class AddInvoiceItemView(generics.CreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            invoice_id = kwargs.get('invoice_id')
            invoice = Invoice.objects.get(pk=invoice_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(invoice=invoice)
            return Response(serializer.data, status=201)
        except Invoice.DoesNotExist:
            return Response({'detail': 'Invoice not found.'}, status=404)


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
        pdf.drawString(100, 800, f'Title: {invoice_item.title}')
        pdf.drawString(100, 780, f'Description: {invoice_item.description}')
        pdf.drawString(100, 760, f'Quantity: {invoice_item.quantity}')
        pdf.drawString(100, 740, f'Unit Price: ${invoice_item.unit_price}')
        pdf.drawString(100, 720, f'Tax: ${invoice_item.tax}')
        pdf.drawString(100, 700, f'Subtotal: ${invoice_item.subtotal}')
        pdf.drawString(100, 680, f'Total: ${invoice_item.total}')
        pdf.save()
        pdf_buffer.seek(0)

        filename = f'invoice_{invoice_item.id}.pdf'
        response = FileResponse(pdf_buffer, as_attachment=True, filename=filename)
        return response

class InvoiceListView(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, sender=self.request.user)

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, sender=self.request.user)

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