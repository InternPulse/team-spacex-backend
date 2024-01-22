from django.urls import path
from .views import GenerateInvoicePDFView

urlpatterns = [
    path('generate_invoice_pdf/<int:pk>/', GenerateInvoicePDFView.as_view(), name='generate_invoice_pdf'),
]
