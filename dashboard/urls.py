# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('metrics/', views.DashboardMetricsView.as_view(), name='dashboard-metrics'),
    # Add more URLs for other dashboard features if needed
]
