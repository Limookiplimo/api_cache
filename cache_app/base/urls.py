from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.products,name="product-list"),
    path("products/category/<str:category>/", views.product_by_category, name="product-by-category"),
    path("products/subcategory/<str:subcategory>/", views.product_by_subcategory, name="product-by-subcategory"),
]
