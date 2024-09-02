from django.contrib import admin
from service.models import Services

class serviceadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_desc')

admin.site.register(Services, serviceadmin)




# Register your models here.
