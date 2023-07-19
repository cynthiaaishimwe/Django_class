from django.db import models

class Reviews(models.Model):
    email=models.EmailField(max_length=32)
    comment=models.TextField()

# Create your models here.
