from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    # products = ["iphone", "imac", "ipad"]
    products = Products.objects.all()  #so this is use to derive data from database
    context = {
       'products' :products
    }
    # return HttpResponse(products)
    return render(request, 'myapp/index.html', context)

def product_detail(request, id):
    pro = Products.objects.get(id=id)  # to get a single product
    context = {
        'product': pro
    }
    return render(request, 'myapp/detail.html', context)

def add_product(request):
    if request.method =='POST':
       name = request.POST.get('name')
       price = request.POST.get('price')
       description = request.POST.get('desc')
       image =request.FILES['upload']
       product = Products(name=name, price=price, desc=description,image=image)
       product.save()
    return render(request, 'myapp/addproduct.html')

def update_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/product')
    context = {
        'product': product,
    }
    return render(request, 'myapp/updateproduct.html', context)

def delete_product(request, id):
    product = Products.objects.get(id=id)
    context = {
        'product': product
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/product')
    return render(request, 'myapp/delete.html', context)

