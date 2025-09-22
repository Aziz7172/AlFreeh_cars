from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
]
