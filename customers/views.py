# customers/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
