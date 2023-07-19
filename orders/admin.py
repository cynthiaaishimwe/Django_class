from django.contrib import admin
from .models import Orders

class OrdersAdmin (admin.ModelAdmin):
    total_display = ("purchaser_name","purchaser_number","vendor_name","vender_number"
    ," product_description"," price"," quantity","basket","customers","shipment")
    
admin.site.register(Orders,OrdersAdmin)


# Register your models here.
