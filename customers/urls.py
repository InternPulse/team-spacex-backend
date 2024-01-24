# customers/urls.py

from django.urls import path
from .views import CustomerListCreateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    # Include any other URLs related to customers
]
