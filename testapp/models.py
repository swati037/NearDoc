from django.db import models

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     #content= models.TextField()
     file = models.FileField(default="")
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)


# class Bloodbank(models.Model):
#      name_site= models.CharField(max_length=255)
#      phone_site= models.CharField(max_length=13)
#     # loc = [('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Banglore', 'Banglore'), ('Navi Mumbai', 'Navi Mumbai')]
#      location = models.CharField(max_length=255,default="")
#      site= models.CharField(max_length=100)