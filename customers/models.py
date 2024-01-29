# customers/models.py

from django.db import models

class Customer(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
    ]

    business_type = models.CharField(max_length=50, default='individual', choices=[('individual', 'Individual'), ('business', 'Business')])
    primary_contact_firstname = models.CharField(max_length=100, blank=True, null=True)
    primary_contact_lastname = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=3, blank=True, null=True)
    email = models.EmailField(unique=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.company_name