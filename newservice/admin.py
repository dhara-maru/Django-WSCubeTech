from django.contrib import admin
from newservice.models import newserviceclass

class newserviceadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_desc')

admin.site.register(newserviceclass, newserviceadmin)

# Register your models here.
