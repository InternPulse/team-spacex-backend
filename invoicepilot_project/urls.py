from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Invoice Pilot API",
        default_version='v1',
        description="API documentation for Invoice Pilot",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
     path('api/', include('myaccount.urls')),
     path('api/', include('invoices.urls')),
     path('api/', include('customers.urls')),  # Adjusted namespace
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]