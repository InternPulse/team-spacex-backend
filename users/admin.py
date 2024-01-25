# users/admin.py

from django.contrib import admin
from .models import Profile, Customer, User, BLToken

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(BLToken)