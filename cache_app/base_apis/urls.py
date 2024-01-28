from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from base_apis import views

urlpatterns = [
    path("api/inventory/",views.InventoryList.as_view()),
    path("api/inventory/<int:pk>/",views.InventoryDetail.as_view()),
    path("api/inventory/category/<str:category>/",views.ProductsByCategory.as_view()),
    path("api/inventory/subcategory/<str:subcategory>/",views.ProductsBySubcategory.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)