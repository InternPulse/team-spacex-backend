# customers/urls.py

from django.urls import path
from .views import CustomerCreateView, CustomerListView

app_name = 'customers'

urlpatterns = [
    path('create-customer/', CustomerCreateView.as_view(), name='customer-create'),
    path('list-customers/', CustomerListView.as_view(), name='customer-list'),
]