# customers/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from users.serializers import ProfileSerializer
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='user.user_profile', read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
