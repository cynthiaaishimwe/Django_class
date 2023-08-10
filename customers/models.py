from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    gender=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    age=models.PositiveBigIntegerField()

