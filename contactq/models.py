from django.db import models

class contactq(models.Model):
    contactq_name = models.CharField(max_length=50)
    contactq_email = models.CharField(max_length=50)
    contactq_phone = models.CharField(max_length=10)
    contactq_website = models.CharField(max_length=100)
    contactq_message = models.TextField()

# Create your models here.
