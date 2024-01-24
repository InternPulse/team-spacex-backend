# invoicepilot_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
     Invoice, PaymentTransaction,
    InvoiceItem, ClientContact, Notification,
    RecurringInvoiceSchedule
)


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'

class InvoiceItemSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    date_created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return InvoiceItem.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RecurringInvoiceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringInvoiceSchedule
        fields = '__all__'

class OurUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
