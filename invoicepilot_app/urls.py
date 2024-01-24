# invoicepilot_app/urls.py

from django.urls import path
from .views import (
    SignUp,
    MyAccount,
    Login,
    InvoiceListCreateView,
    DashboardAPIView,
    PaymentTransactionListCreateView,
    InvoiceItemListCreateView,
    ClientContactListCreateView,
    NotificationListCreateView,
    RecurringInvoiceScheduleListCreateView,
    TestMailerView,
)
from customers.views import CustomerListCreateView  # Import from the correct location

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('myaccount/', MyAccount.as_view(), name='myaccount'),
    path('login/', Login.as_view(), name='login'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard-api'),
    path('payment-transactions/', PaymentTransactionListCreateView.as_view(), name='payment-transaction-list-create'),
    path('invoice-items/', InvoiceItemListCreateView.as_view(), name='invoice-item-list-create'),
    path('client-contacts/', ClientContactListCreateView.as_view(), name='client-contact-list-create'),
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('recurring-invoice-schedules/', RecurringInvoiceScheduleListCreateView.as_view(), name='recurring-invoice-schedule-list-create'),
    path('test-mailer/', TestMailerView.as_view(), name='test-mailer'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),  # Add this line for the customers view
    # Add more URLs as needed
]
