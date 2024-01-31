# invoices/serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceItem

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceEmptySerializer(serializers.Serializer):
    pass

from rest_framework import serializers

class SendInvoiceEmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255, required=False, default='Invoice Notification')
    pdf_content = serializers.FileField()
