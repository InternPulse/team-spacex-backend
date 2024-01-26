
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
from rest_framework.authtoken.models import Token

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'business_name', 'business_category', 'transaction_currency')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class NewUserCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    
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
                raise ValidationError('Unable to log in with provided credentials. Please use your email and password')
        else:
            raise ValidationError('Must include "email" and "password".')

        
class UserManageSerializer(ModelSerializer):  
    email = EmailField(required=False)
    username = CharField(required=False, validators=[v.validate_name])  
    class Meta:
        model = User
        fields = ['email', 'username', 'id']
        read_only_fields = ['id']

class RequestSerializer(Serializer):
    email = EmailField()

class PasswordResetSerializer(Serializer):
    password = CharField(validators=[v.validate_password])
    confirm_password = CharField(validators=[v.validate_password])

class EmptySerializer(Serializer):
    pass
