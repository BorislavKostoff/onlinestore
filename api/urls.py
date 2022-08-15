from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addProduct),
    path('api/stats', views.orderStats),
    path('order/', views.addOrder),
]