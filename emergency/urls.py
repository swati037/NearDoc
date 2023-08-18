from . import views
from . views import emerg
from django.urls import path

urlpatterns = [
    path('emerg', views.emerg, name = "emerg")
]