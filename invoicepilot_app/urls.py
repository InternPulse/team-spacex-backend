# invoicepilot_app/urls.py

from django.urls import path
from .views import SignUp, MyAccount, Login, InvoiceListCreateView, DashboardAPIView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('myaccount/', MyAccount.as_view(), name='myaccount'),
    path('login/', Login.as_view(), name='login'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard-api'),
    # Add more URLs as needed
]
