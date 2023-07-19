from django.contrib import admin

from .models import Delivery
class DeliveryAdmin (admin.ModelAdmin):
    total_display = ("latitude"," longitude","location_name","address")
admin.site.register(Delivery,DeliveryAdmin)


# Register your models here.
