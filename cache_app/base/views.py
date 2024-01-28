from django.shortcuts import render
import requests

def products(request):
    data = requests.get(f"http://127.0.0.1:8000/api/inventory")
    products = data.json()
    context = {"products": products}
    return render(request, "base/inventory.html",context)

def search_products(request):
    search_term = request.GET.get('search')
    
    if not search_term:
        data = requests.get("http://127.0.0.1:8000/api/inventory")
        products = data.json()
    else:
        products_endpoint = f"http://127.0.0.1:8000/api/inventory/product/{search_term}/"
        category_endpoint = f"http://127.0.0.1:8000/api/inventory/category/{search_term}/"
        subcategory_endpoint = f"http://127.0.0.1:8000/api/inventory/subcategory/{search_term}/"
        
        product_data = requests.get(products_endpoint).json()
        category_data = requests.get(category_endpoint).json()
        subcategory_data = requests.get(subcategory_endpoint).json()

        if product_data:
            products = product_data
        elif category_data:
            products = category_data
        elif subcategory_data:
            products = subcategory_data
        else:
            products = []
    
    context = {"products": products}
    return render(request, "base/inventory.html", context)