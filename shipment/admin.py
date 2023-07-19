from django.contrib import admin

from .models import Shipment

class ShipmentAdmin (admin.ModelAdmin):
    total_display = ("shipping_cost"," tracking_number "," recipient_address","recipient_contact_info ")
admin.site.register(Shipment,ShipmentAdmin)
