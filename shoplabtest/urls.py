from . import views
from django.urls import path

urlpatterns = [
    path('', views.labtest, name = "labtest"),
    path('tracker', views.tracker, name = "tracker"),
    path('search', views.search, name = "search"),
    path('productiew', views.productview, name = "productview"),
    path('checkout', views.checkout, name = "checkout"),
    path('products/<int:myid>', views.productview, name="ProductView"),
]