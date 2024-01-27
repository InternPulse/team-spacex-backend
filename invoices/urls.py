from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceCreateView,
    AddInvoiceItemView,
    GenerateInvoicePDFView,
    SendInvoiceEmailView,
    InvoiceItemListView,
)

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/add-item/<int:invoice_id>/', AddInvoiceItemView.as_view(), name='add-invoice-item'),
    path('invoices/create-invoice/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:invoice_id>/items/', InvoiceItemListView.as_view(), name='invoice-item-list'),  # Use InvoiceItemListView here
    path('invoices/generate-pdf/<int:pk>/', GenerateInvoicePDFView.as_view(), name='generate-invoice-pdf'),
    path('invoices/send-email/<int:pk>/', SendInvoiceEmailView.as_view(), name='send-invoice-email'), 
]
