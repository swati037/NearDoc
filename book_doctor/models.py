from distutils.log import Log
from django.db import models
from login.models import log, logd
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=50)
    spc = [
        ('Dentist', 'Dentist'),
        ('Gynecologist', 'Gynecologist'),
        ('General Physician', 'General Physician'),
        ('ENT Specialist', 'ENT Specialist'),
    ]
    specialist = models.CharField(max_length=30, choices = spc)
    experience = models.IntegerField()         

    def __str__(self):
        return self.name

class VidDoc(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.doctor.name

class VidApp(models.Model):
    viddoc = models.ForeignKey(VidDoc, on_delete=models.CASCADE)
    tm = [
        (0, '09:00 - 09:30'),
        (1, '10:00 - 10:30'),
        (2, '11:00 - 11:30'),
        (3, '12:00 - 12:30'),
        (4, '13:00 - 13:30'),
        (5, '14:00 - 14:30'),
        (6, '15:00 - 15:30'),
        (7, '16:00 - 16:30'),
        (8, '17:00 - 17:30'),        
    ]
    time = models.IntegerField(choices=tm)

    def __str__(self):
        return str(self.viddoc.doctor.name) + '-' + str(self.time)

class VAppointment(models.Model):
    log = models.ForeignKey(log, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    tslot = models.CharField(max_length=30)
    date = models.DateField()
    link = models.URLField()
    pword = models.CharField(max_length=20)

    def __str__(self):
        return str(self.doctor.name) + '-' + str(self.log.username)