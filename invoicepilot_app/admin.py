from django.contrib import admin
from .models import (
    Profile, Invoice, PaymentTransaction,
    InvoiceItem, ClientContact, Notification,
    RecurringInvoiceSchedule, MailRecord
)
admin.site.register(Profile)
admin.site.register(Invoice)
admin.site.register(PaymentTransaction)
admin.site.register(InvoiceItem)
admin.site.register(ClientContact)
admin.site.register(Notification)
admin.site.register(RecurringInvoiceSchedule)
admin.site.register(MailRecord)