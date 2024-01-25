# invoices/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Customer, Invoice, InvoiceItem
from .serializers import CustomerSerializer, InvoiceSerializer, InvoiceItemSerializer
from django.shortcuts import render
from django.utils import timezone
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from invoices.models import InvoiceItem  # Assuming 'invoices' is the correct app name
from django.http import FileResponse
from io import BytesIO

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
    serializer_class = CustomerSerializer
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
