# dashboard/serializers.py
from rest_framework import serializers

class DashboardMetricsSerializer(serializers.Serializer):
    total_receivables = serializers.IntegerField()
    total_sales = serializers.IntegerField()
    overdue_invoices = serializers.IntegerField()
    total_receipts = serializers.DecimalField(max_digits=10, decimal_places=2)
