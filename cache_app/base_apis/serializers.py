from rest_framework import serializers
from base_apis.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["product","price","category","subcategory"]



