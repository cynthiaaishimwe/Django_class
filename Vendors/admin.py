from django.contrib import admin

from .models import Vendor
class VendorAdmin (admin.ModelAdmin):
    total_display = ("name","gender","last_name","email","age")
admin.site.register(Vendor,VendorAdmin)


# Register your models here.
