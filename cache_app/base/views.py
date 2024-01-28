from django.shortcuts import render
import requests

def products(request):
    data = requests.get(f"http://127.0.0.1:8000/api/inventory")
    products = data.json()
    print(products)
    context = {"products": products}
    return render(request, "base/inventory.html",context)

def product_by_category(request, category):
    response = requests.get(f"http://127.0.0.1:8000/api/inventory/category/{category}/")
    products = response.json()
    context = {"products": products}
    return render(request, "base/inventory.html",context)

def product_by_subcategory(request, subcategory):
    response = requests.get(f"http://127.0.0.1:8000/api/inventory/subcategory/{subcategory}/")
    products = response.json()
    context = {"products": products}
    return render(request, "base/inventory.html",context)
