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
    url='https://reimagined-memory-qj6r65pvrrrcxpw6-8000.app.github.dev' # Ignore this line
)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('auth/', include('users.urls')),
     path('api/', include('invoices.urls')),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]