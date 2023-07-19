from django.db import models


class Shipment(models.Model):
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tracking_number = models.CharField(max_length=50, unique=True)
    recipient_address = models.CharField(max_length=200)
    recipient_contact_info = models.CharField(max_length=100)



