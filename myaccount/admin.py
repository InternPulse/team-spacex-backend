from django.contrib import admin
from .models import Profile, User, BLToken

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(BLToken)