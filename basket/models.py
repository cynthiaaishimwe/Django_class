from django.db import models

class Basket(models.Model):
  product_name=models.CharField(max_length=32)
  price=price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity_in_kilograms = models.DecimalField(max_digits=10, decimal_places=2)
    