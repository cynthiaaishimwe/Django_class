from django.db import models
from Vendors.models import Vendor

class Product(models.Model):
    Vendor = models.ForeignKey(Vendor,null= True, on_delete = models.CASCADE)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField()
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

# Create your models here.
