from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils.crypto import constant_time_compare
from datetime import timedelta
class User(AbstractUser):
    """Custom user model. This user class is what we will be using"""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"User: {self.id} - {self.email}"
    
    def save(self, *args, **kwargs) -> None:
        self.updated_at = now()
        return super().save(*args, **kwargs)

class BLToken(models.Model):
    key = models.CharField(max_length=255, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Blacklisted Token: {self.id} for {self.user.email}"

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


