from django.db import models

class Delivery(models.Model):
    company_name=models.CharField(max_length=32)
    delivery_person=models.CharField(max_length=32)
    recipient_name=models.CharField(max_length=32)
    delivery_order_number=models.CharField(max_length=32)

# Create your models here.
