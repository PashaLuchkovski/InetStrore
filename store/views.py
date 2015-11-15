from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def productList(request):
    return render(request, "ProductList.html")

def product(request, productID):
    return render(request, 'Product.html', {'product' : ''})

def admin(request):
    return render(request, "Admin.html")

def checker(request, name):
    return render(request, "Checker.html", {'name': name})