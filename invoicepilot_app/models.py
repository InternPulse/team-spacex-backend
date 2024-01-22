# invoicepilot_app/models.py

from django.db import models
from django.contrib.auth.models import User

class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

class InvoiceItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    invoice_date_generated = models.DateTimeField(auto_now=True)
    
    @property
    def total_price_calc(self):
        self.total_price = self.quantity * self.price
        self.save()
        return self.total_price
        
class ClientContact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
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
    recipent = models.ForeignKey('ClientContact', on_delete=models.SET_NULL, null=True)
    recipent_email = models.EmailField(null=True) # In case client information is deleted so we still have access to who the invoice was prepared for # Add more fields as needed

class MailRecord(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='mail_records')
    to = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)
    template_used = models.CharField(max_length=20, default='default')
    # Add more fields as needed