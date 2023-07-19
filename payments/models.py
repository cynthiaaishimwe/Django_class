from django.db import models

class Payment(models.Model):
    payee_name=models.CharField(max_length=32)
    payee_address=models.CharField(max_length=32)
    payment_amount=models.CharField(max_length=32)









# Create your models here.
