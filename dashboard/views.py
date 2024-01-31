#dashboard/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated
from .serializers import DashboardMetricsSerializer
from invoices.models import Invoice
from django.utils import timezone

class DashboardMetricsView(APIView):
    permission_classes = [IsAuthenticated]  # Add permission class to ensure user is authenticated

    def get(self, request):
        # Filter invoices based on the logged-in user
        user_invoices = Invoice.objects.filter(user=request.user)
        
        total_receivables = user_invoices.filter(status='pending').count()
        total_sales = user_invoices.filter(status='paid').count()
        overdue_invoices = user_invoices.filter(status='pending', due_date__lt=timezone.now()).count()
        total_receipts = 0  # Implement logic to calculate total receipts

        data = {
            'total_receivables': total_receivables,
            'total_sales': total_sales,
            'overdue_invoices': overdue_invoices,
            'total_receipts': total_receipts,
        }
        serializer = DashboardMetricsSerializer(data)
        return Response(serializer.data)
