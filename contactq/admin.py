from django.contrib import admin
from contactq.models import contactq
class contactqadmin(admin.ModelAdmin):
    list_display=('contactq_name','contactq_email','contactq_phone', 'contactq_website', 'contactq_message')
    
admin.site.register(contactq, contactqadmin)
# Register your models here.
