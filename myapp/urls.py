
from django.contrib import admin
from django.urls import path

from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index),
    path('product/', views.products, name='product'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/edit/<int:id>/', views.update_product, name='update_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product')
]
