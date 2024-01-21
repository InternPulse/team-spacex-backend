# invoicepilot_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Profile, Invoice, PaymentTransaction,
    InvoiceItem, ClientContact, Notification,
    RecurringInvoiceSchedule
)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

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

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
