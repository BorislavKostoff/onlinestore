from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addProduct),
    path('api/stats', views.OrderAPIView.as_view()),
    path('order/', views.addOrder),
]