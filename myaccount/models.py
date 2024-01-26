#myaccount/models.py
from django.db import models
from django.contrib.auth.models import User

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