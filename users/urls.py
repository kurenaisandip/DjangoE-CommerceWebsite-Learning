
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as authentication_views

from . import views
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', authentication_views.LoginView.as_view(), name='login')  #class based view: whenever we are using the classbased view, we need to need to mention the view
]
