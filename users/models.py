# users/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    business_category = models.CharField(
        max_length=50,
        choices=[
            ('individual', 'Individual/Freelancer'),
            ('accounting', 'Accounting and Bookkeeping'),
            # ... other choices ...
        ]
    )
    transaction_currency = models.CharField(max_length=3)
    customers = models.ManyToManyField('Customer', related_name='profile_customers', blank=True)

    def __str__(self):
        return self.full_name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_user', null=True)
    customer_type = models.CharField(max_length=20, choices=[('Business', 'Business'), ('Individual', 'Individual')], default='Individual')
    primary_contact_first_name = models.CharField(max_length=30, default='DefaultFirstName')
    primary_contact_last_name = models.CharField(max_length=30, default='DefaultLastName')
    company_name = models.CharField(max_length=100, default='DefaultCompanyName')
    currency = models.CharField(max_length=3, default='USD')
    customer_email = models.EmailField(default='default@example.com')
    customer_phone_work = models.CharField(max_length=15, blank=True, null=True, default='DefaultPhoneWork')
    customer_phone_mobile = models.CharField(max_length=15, blank=True, null=True, default='DefaultPhoneMobile')

    def __str__(self):
        return self.primary_contact_first_name + ' ' + self.primary_contact_last_name


