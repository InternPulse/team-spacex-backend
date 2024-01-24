# users/urls.py

from django.urls import path
from .views import SignUp, Login, CreateProfile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('create-profile/', CreateProfile.as_view(), name='create-profile'),
    # Add more URLs as needed
]
