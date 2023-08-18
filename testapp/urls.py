from . import views
from django.urls import path

urlpatterns = [
    path('appoint/', views.contact, name = "test"),
    path('finance/', views.finance, name = "finance"),
    path('bloodbank/', views.bloodbank, name = "bloodbank"),
]