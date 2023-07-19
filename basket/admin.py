from django.contrib import admin

from .models import Basket
class BasketAdmin (admin.ModelAdmin):
    total_display = ("first_name","last_name","price","quantity_in_kilograms")
admin.site.register(Basket,BasketAdmin)
# Register your models here.
