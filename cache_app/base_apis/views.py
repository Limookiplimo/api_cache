from base_apis.models import Inventory
from base_apis.serializers import InventorySerializer
from rest_framework import generics

# Create your views here.
class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class ProductsByCategory(generics.ListAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        category = self.kwargs["category"]
        return Inventory.objects.filter(category=category)
    
class ProductsBySubcategory(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        subcategory = self.kwargs["subcategory"]
        return Inventory.objects.filter(subcategory=subcategory)

class ProductByName(generics.ListAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        product = self.kwargs["product"]
        return Inventory.objects.filter(product=product)
