# invoicepilot_app/models.py

from django.db import models
from django.contrib.auth.models import User

class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed

class ClientContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Add more fields as needed

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

class RecurringInvoiceSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=20)
    # Add more fields as needed

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add profile fields as needed

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed
