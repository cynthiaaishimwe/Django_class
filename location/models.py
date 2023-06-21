from django.db import models

class Locations(models.Model):
    latitude=models.FloatField(max_length=32)
    longitude=models.FloatField(max_length=32)
    location_name=models.CharField(max_length=32)
    address=models.CharField(max_length=32)
    
# Create your models here.
