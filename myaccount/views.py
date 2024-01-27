from rest_framework.generics import CreateAPIView, GenericAPIView
from .models import BLToken, Profile 
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .backends import CustomJWTAuthentication
from django.dispatch import receiver
from django.conf import settings
from utils.mailer import Mailer
from rest_framework_simplejwt.tokens import RefreshToken
from utils.encrypt import generate_otps, verify_otps, pwd_reset_token_created
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import (
    NewUserCreateSerializer,
    CustomAuthTokenSerializer, RequestSerializer, 
    PasswordResetSerializer, EmptySerializer,
    ProfileSerializer, UserManageSerializer
)
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)

User = get_user_model()
my_mailer = Mailer()
class CreateProfile(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class LoginView(TokenObtainPairView):
    serializer_class = CustomAuthTokenSerializer


class SignupView(CreateAPIView):
    serializer_class = NewUserCreateSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            token = generate_otps(user.id, 'vyf')
            link = f"{settings.API_URL}/auth/activate/{token}"
            my_mailer.send_email(
                "Welcome to InvoicePilot",
                user.email, "welcome",
                {"user": user.username, "link": link}
            )
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.perform_create(serializer)


class LogoutView(TokenBlacklistView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomJWTAuthentication,)
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        header = request.headers.get('Authorization')
        token = header.split(' ')[1]
        BLToken.objects.create(key=token, user=request.user)
        return response

class RefreshTokenView(TokenRefreshView):
    pass

class PasswordResetRequestView(GenericAPIView):
    serializer_class = RequestSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = generate_otps(user.id, 'pwd')
            link = f"{settings.API_URL}/auth/reset-password/{token}"
            sent = my_mailer.send_email(
                "Password Reset", user.email, "pwd_reset",
                {'user': user.username, 'link': link})
            pwd_reset_token_created.send(sender=self.__class__, instance=self, token=token, user_email=user.email)
            if sent:
                return Response({"message": "A reset password token has been sent to your email"}, status=HTTP_200_OK)
            else:
                return Response({"message": "An error occurred. Please try again later"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message": "There's no user with this email"}, status=HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        token = kwargs.get('token', "")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        pwd = serializer.validated_data.get('password')
        _pwd = serializer.validated_data.get('confirm_password')

        user, status = verify_otps(token, 'pwd')

        if status == 400:
            return Response({'status': 'invalid or expired token'}, status=HTTP_400_BAD_REQUEST)
        if status == 400:
            return Response({'status': 'User does not exist. May have been deleted'}, status=HTTP_404_NOT_FOUND)
        if pwd != _pwd:
            return Response({'status': 'passwords do not match'}, status=HTTP_400_BAD_REQUEST)
        user.set_password(pwd)
        user.save()
        return Response({'status': 'success'}, status=HTTP_200_OK)


class RequestVerificationView(GenericAPIView):
    serializer_class = RequestSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = generate_otps(user.id, 'vyf')
            link = f"{settings.API_URL}/auth/activate/{token}"
            sent = my_mailer.send_email(
                "Verify your account",
                user.email, "verify",
                {"user": user.username, "link": link}
            ) 
            if sent:           
                return Response({"message": "A verification token has been sent to your email"}, status=HTTP_200_OK)
            else:
                return Response({"message": "An error occurred. Please try again later"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message": "There's no user with this email"}, status=HTTP_400_BAD_REQUEST)

class VerificationConfirmView(GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = EmptySerializer
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token', "")
        user, status = verify_otps(token, 'vyf')
        if status == 400:
            return Response({'status': 'invalid or expired token'}, status=HTTP_400_BAD_REQUEST)
        if not user:
            return Response({'status': 'User does not exist. May have been deleted'}, status=HTTP_404_NOT_FOUND)
        user.is_verified = True
        user.save()
        return Response({'status': 'success'}, status=HTTP_200_OK)

# class CreateProfile(CreateAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
class UserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserManageSerializer
    

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response(self.serializer_class(user).data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response({}, status=HTTP_204_NO_CONTENT)
