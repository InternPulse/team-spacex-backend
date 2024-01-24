# customers/admin.py

from django.contrib import admin
from .models import Customer, Invoice, InvoiceItem

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)