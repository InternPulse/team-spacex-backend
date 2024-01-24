# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    business_name = serializers.CharField(write_only=True)
    business_category = serializers.ChoiceField(
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
        ],
        write_only=True,
    )
    transaction_currency = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'full_name', 'business_name', 'business_category', 'transaction_currency')
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'YourUserCreateSerializer',

    def create(self, validated_data):
        # Extract profile data from validated_data
        profile_data = {
            'full_name': validated_data.pop('full_name', 'Default Full Name'),
            'business_name': validated_data.pop('business_name', 'Default Business Name'),
            'business_category': validated_data.pop('business_category', 'individual'),
            'transaction_currency': validated_data.pop('transaction_currency', 'USD'),
        }

        # Explicitly set the email field
        email = validated_data.pop('email', None)

        # Create a new user
        user = User.objects.create_user(email=email, **validated_data)

        # Create a new profile for the user
        Profile.objects.create(user=user, **profile_data)

        return user



class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)
