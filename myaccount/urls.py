from django.urls import path
from .views import (
    LoginView, LogoutView, SignupView, RefreshTokenView,
    RequestVerificationView, PasswordResetRequestView,
    PasswordResetConfirmView, VerificationConfirmView, UserView
)

urlpatterns = [
    # path('create-profile/', CreateProfile.as_view(), name='create-profile'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('refresh-token', RefreshTokenView.as_view(), name='refresh-token'),
    path('signup', SignupView.as_view(), name="signup"),
    path('resend_activation', RequestVerificationView.as_view(), name='request-verification'),
    path('activate/<str:token>', VerificationConfirmView.as_view(), name='verify'),
    path('request-password-reset', PasswordResetRequestView.as_view(), name='password-reset'),
    path('reset_password/<str:token>', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('user/me', UserView.as_view(), name='user-me'),
]