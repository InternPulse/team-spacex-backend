
from rest_framework import serializers
from .models import Profile
from rest_framework.serializers import (
    ModelSerializer, Field, EmailField,
    ValidationError, Serializer,
    CharField
)
import  utils.validators as v
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'business_name', 'business_category', 'transaction_currency')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class NewUserCreateSerializer(ModelSerializer):
    first_name = CharField(write_only=True, validators=[v.validate_name])
    last_name = CharField(write_only=True, validators=[v.validate_name])
    username = CharField(validators=[v.validate_name])
    password = CharField(validators=[v.validate_password])
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')
        user = User.objects.create_user(**validated_data, first_name=first_name, last_name=last_name)
        return user


class CustomAuthTokenSerializer(Serializer):
    email = CharField(validators=[v.validate_name])
    password = CharField(validators=[v.validate_password])

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = User.objects.filter(email=email).first()
            if not user:
                user = User.objects.filter(username=email).first()
            if user and user.check_password(password):
                result = {}
                refresh = self.get_token(user)
                result["refresh"] = str(refresh)
                result["access"] = str(refresh.access_token)
                update_last_login(None, user)
                return result
            else:
                raise ValidationError('Invalid email/username or password')
        else:
            raise ValidationError('Must include "email" and "password".')
    
    @classmethod
    def get_token(cls, user) -> Token:
        return RefreshToken.for_user(user)
        
class UserManageSerializer(ModelSerializer):  
    email = EmailField(required=False)
    username = CharField(required=False, validators=[v.validate_name])  
    first_name = CharField(required=False, validators=[v.validate_name])  
    last_name = CharField(required=False, validators=[v.validate_name])  
    class Meta:
        model = User
        fields = ['email', 'username', 'id', 'first_name', 'last_name']
        read_only_fields = ['id']

class RequestSerializer(Serializer):
    email = EmailField()

class PasswordResetSerializer(Serializer):
    password = CharField(validators=[v.validate_password])
    confirm_password = CharField(validators=[v.validate_password])

class EmptySerializer(Serializer):
    pass
