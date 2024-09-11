from django.contrib import admin

from login.models import loginclass
class loginadmin(admin.ModelAdmin):
    list_display=('login_username','login_email','login_password')
# Register your models here.


admin.site.register(loginclass, loginadmin)