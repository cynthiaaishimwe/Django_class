from django.db import models

class Contact(models.Model):
    phone_number=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    address=models.CharField(max_length=32)
    social_medias=models.URLField(max_length=32)
    

# Create your models here.
