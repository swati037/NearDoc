from . import views
from django.urls import path

urlpatterns = [
    path('search_doc', views.search_doc, name = "search_doc"),
    path('select_date', views.select_date, name = "select_date"),
    path('select_slot', views.select_slot, name = "select_slot"),
    path('vid_details', views.vid_details, name = "vid_details"),
    path('vd_mpay', views.vd_mpay, name = "vd_mpay"),
]

