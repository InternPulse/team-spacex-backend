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
            ('agriculture', 'Agriculture'),
            ('association', 'Association/Club'),
            ('automobile', 'Automobile'),
            ('business_consulting', 'Business Consulting'),
            ('clinic_healthcare', 'Clinic and Healthcare Services'),
            ('construction_engineering', 'Construction and Engineering'),
            ('education', 'Education'),
            ('technology', 'Technology'),
            # Add more choices as needed
        ]
    )
    transaction_currency = models.CharField(max_length=3)  # Assuming a 3-letter currency code, e.g., USD

    def __str__(self):
        return self.full_name
