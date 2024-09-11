from django.db import models

class loginclass(models.Model):
    login_username = models.CharField(max_length=50)
    login_email = models.CharField(max_length=50)
    login_password = models.CharField(max_length=50)
    
    
    