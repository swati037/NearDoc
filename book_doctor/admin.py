from django.contrib import admin

from .models import Doctor, VidApp, VidDoc, VAppointment
# Register your models here.

admin.site.register(Doctor)
admin.site.register(VidDoc)
admin.site.register(VidApp)
admin.site.register(VAppointment)