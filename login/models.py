from django.db import models

# Create your models here.
class log(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
class logd(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    veri = models.CharField(max_length=50, default="No")
    