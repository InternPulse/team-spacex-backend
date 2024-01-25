# invoices/models.py
from django.db import models
from django.contrib.auth.models import User

class MailRecord(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    to = models.EmailField()
    template_used = models.CharField(max_length=255)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invoices')
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='received_invoices', null=True, blank=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('flutterwave', 'Flutterwave'),
        ('paystack', 'Paystack'),
        ('paypal', 'PayPal'),
        ('card', 'Credit Card'),
    ])
    status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('not_paid', 'Not Paid'),
        ('failed', 'Failed'),
    ], default='pending')

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)