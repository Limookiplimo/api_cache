from django.db import models

# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)

    class Meta:
        ordering = ['category']
