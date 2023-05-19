from django.contrib import admin
from .models import Products

# Register your models here.
admin.site.register(Products)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("Hello World")
#
# def products(request):
#     # products = ["iphone", "imac", "ipad"]
#     products = Products.objects.all()  #so this is use to derive data from database
#     return HttpResponse(products)

