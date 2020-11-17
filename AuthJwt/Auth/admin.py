from django.contrib import admin

# Register your models here.
from Auth.models import User, AccessControl

admin.register(User)
admin.register(AccessControl)
