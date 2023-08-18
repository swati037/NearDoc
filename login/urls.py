from . import views
from django.urls import path

urlpatterns = [
    path('', views.land, name = "landing"),
    path('loginp', views.loginP, name = "loginPatients"),
    path('logind', views.loginD, name = "loginDoctor"),
    path('loginPa', views.loginPa, name = "loginPatients"),
    path('loginDr', views.loginDr, name = "loginDoctor"),
    path('registration', views.registration, name = "registration"),
    path('registrationd', views.registrationD, name = "registrationd"),
    #path('labtest', views.labtest, name = "labtest"),
    path('contact', views.cont, name = "contact"),
    path('home', views.home, name = "home"),
    path('logout',views.logout, name="logout"),
    path('logoutDr',views.logoutDr, name="logoutDr")
]