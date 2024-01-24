# invoices/urls.py
from django.urls import path
from .views import CustomerListCreateView, InvoiceListCreateView, InvoiceItemCreateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:invoice_id>/items/', InvoiceItemCreateView.as_view(), name='invoice-item-create'),
]
