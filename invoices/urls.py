from django.urls import path
from .views import CustomerListCreateView, InvoiceListCreateView, InvoiceItemCreateView, GenerateInvoicePDFView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:invoice_id>/items/', InvoiceItemCreateView.as_view(), name='invoice-item-create'),
    path('invoices/generate-pdf/<int:pk>/', GenerateInvoicePDFView.as_view(), name='generate-invoice-pdf'),
]
