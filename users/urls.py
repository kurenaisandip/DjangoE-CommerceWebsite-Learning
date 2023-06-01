
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as authentication_views

from . import views
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),  #class based view: whenever we are using the classbased view, we need to need to mention the view
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='createprofile'),
    path('sellerprofile/<int:id>', views.seller_profile, name = 'sellerprofile'),
]
