clear# invoices/urls.py
from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceCreateView,
    AddInvoiceItemView,  # Update this line
    GenerateInvoicePDFView,
    SendInvoiceEmailView,
)


urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
     path('invoices/add-item/<int:invoice_id>/', AddInvoiceItemView.as_view(), name='add-invoice-item'),
    path('invoices/create-invoice/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:invoice_id>/items/', InvoiceCreateView.as_view(), name='invoice-item-create'),
    path('invoices/generate-pdf/<int:pk>/', GenerateInvoicePDFView.as_view(), name='generate-invoice-pdf'),
    path('invoices/send-email/<int:pk>/', SendInvoiceEmailView.as_view(), name='send-invoice-email'), 
]
