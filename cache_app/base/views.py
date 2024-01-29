from django.shortcuts import render
from requests_cache.session import CachedSession
from datetime import timedelta
import os

def products(request):
    session = CachedSession("../database/cache/inventory_cache", expire_after=timedelta(hours=1))
    data = session.get(f"http://127.0.0.1:8000/api/inventory")
    products = data.json()
    context = {"products": products}
    return render(request, "base/inventory.html",context)

def search_products(request):
    search_term = request.GET.get('search')
    session = CachedSession("../database/cache/inventory_cache", expire_after=timedelta(hours=1))
    
    if not search_term:
        data = session.get("http://127.0.0.1:8000/api/inventory")
        products = data.json()
    else:
        products_endpoint = f"http://127.0.0.1:8000/api/inventory/product/{search_term}/"
        category_endpoint = f"http://127.0.0.1:8000/api/inventory/category/{search_term}/"
        subcategory_endpoint = f"http://127.0.0.1:8000/api/inventory/subcategory/{search_term}/"
        
        product_data = session.get(products_endpoint).json()
        category_data = session.get(category_endpoint).json()
        subcategory_data = session.get(subcategory_endpoint).json()

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