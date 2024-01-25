# users/serializers.py

from rest_framework import serializers
from .models import Profile, Customer
from rest_framework.serializers import (
    ModelSerializer, Field, EmailField,
    ValidationError, Serializer,
    CharField
)
import  utils.validators as v
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('user',)

class ProfileSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class NewUserCreateSerializer(serializers.ModelSerializer):
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
        try:
            user = User.objects.create_user(email=email, **validated_data)
        except IntegrityError as e:
            print(e)
            raise ValidationError("A user with this email already exists")
        # Create a new profile for the user
        Profile.objects.create(user=user, **profile_data)

        return user



class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

class CustomAuthTokenSerializer(Serializer):
    email = EmailField()
    password = CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                attrs['user'] = user
                return attrs
            else:
                raise ValidationError('Unable to log in with provided credentials.')
        else:
            raise ValidationError('Must include "email" and "password".')



# class UserSerializer(ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'first_name', 'id',
#                   'last_name', 'created_at']
#         read_only_fields = ['id']
        
class UserManageSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'id',
                  'last_name', 'created_at',
                ]
        read_only_fields = ['id', 'created_at']

class RequestSerializer(Serializer):
    email = EmailField()

class PasswordResetSerializer(Serializer):
    password = CharField(validators=[v.validate_password])
    confirm_password = CharField(validators=[v.validate_password])

class EmptySerializer(Serializer):
    pass
