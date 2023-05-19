
from django.contrib import admin
from django.urls import path

from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index),
    path('product/', views.products),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]
