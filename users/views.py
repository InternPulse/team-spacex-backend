# users/views.py

from rest_framework import generics, permissions
from .models import Profile 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import NewUserCreateSerializer, UserLoginSerializer, ProfileSerializer
from django.contrib.auth import authenticate, get_user_model

class SignUp(generics.CreateAPIView):
    serializer_class = NewUserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        # Check if the user was created through the API and not the admin interface
        if 'api' in self.request.path:
            # Create a profile for the user if it doesn't exist
            Profile.objects.get_or_create(user=user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class Login(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_email = serializer.validated_data['username_or_email']
        password = serializer.validated_data['password']

        # Try to authenticate with username
        user = authenticate(request, username=username_or_email, password=password)

        if user is None:
            # If authentication fails with username, try with email
            user = authenticate(request, email=username_or_email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)

class CreateProfile(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
