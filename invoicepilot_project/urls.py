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
        url="https://psychic-meme-5j5657xvpw5297q-8000.app.github.dev/"


),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('auth/', include('myaccount.urls')),
     path('api/', include('invoices.urls')),
     path('api/', include('customers.urls')),
     path('api/dashboard/', include('dashboard.urls')),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]