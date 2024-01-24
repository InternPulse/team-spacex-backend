# customers/models.py

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_type = models.CharField(max_length=20, choices=[('Business', 'Business'), ('Individual', 'Individual')], default='Individual')
    primary_contact_first_name = models.CharField(max_length=30, default='DefaultFirstName')
    primary_contact_last_name = models.CharField(max_length=30, default='DefaultLastName')
    company_name = models.CharField(max_length=100, default='DefaultCompanyName')
    currency = models.CharField(max_length=3, default='USD')  # Default currency code, e.g., USD
    customer_email = models.EmailField(default='default@example.com')  # Set a default email address
    customer_phone_work = models.CharField(max_length=15, blank=True, null=True, default='DefaultPhoneWork')
    customer_phone_mobile = models.CharField(max_length=15, blank=True, null=True, default='DefaultPhoneMobile')

    def __str__(self):
        return self.user.username
