clear# invoices/urls.py
from django.urls import path
from .views import (
    CustomerListCreateView,
    InvoiceListCreateView,
    InvoiceItemCreateView,
    GenerateInvoicePDFView,
    SendInvoiceEmailView,  # Add the new view
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:invoice_id>/items/', InvoiceItemCreateView.as_view(), name='invoice-item-create'),
    path('invoices/generate-pdf/<int:pk>/', GenerateInvoicePDFView.as_view(), name='generate-invoice-pdf'),
    path('invoices/send-email/<int:pk>/', SendInvoiceEmailView.as_view(), name='send-invoice-email'),  # New endpoint
]
