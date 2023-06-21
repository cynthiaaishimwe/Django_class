from django.contrib import admin

from .models import Locations
class LocationsAdmin (admin.ModelAdmin):
    total_display = ("latitude"," longitude","location_name","address")
admin.site.register(Locations,LocationsAdmin)

# Register your models here.
