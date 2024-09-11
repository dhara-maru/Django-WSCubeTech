from django.contrib import admin
from .models import loginclass

class loginadmin(admin.ModelAdmin):
    list_display = ('login_username', 'login_email', 'login_password')

admin.site.register(loginclass, loginadmin)
