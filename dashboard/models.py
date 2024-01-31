from django.db import models
from django.conf import settings

class DashboardData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_receivables = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    overdue_invoices = models.IntegerField(default=0)
    total_receipts = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Dashboard Data for {self.user.username}"
