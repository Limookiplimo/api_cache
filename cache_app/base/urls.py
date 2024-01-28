from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.products,name="product-list"),
    path('products/search-products/', views.search_products, name='search-products'),
]