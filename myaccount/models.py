from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils.crypto import constant_time_compare
from datetime import timedelta


class User(AbstractUser):
    """Custom user model. This user class is what we will be using"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
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
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    business_category = models.CharField(
        max_length=50,
        choices=[
            ('individual', 'Individual/Freelancer'),
            ('Business', 'Business/Company'),

        ]
    )
    transaction_currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name