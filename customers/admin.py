from django.contrib import admin

from .models import Customer
class CustomerAdmin (admin.ModelAdmin):
    total_display = ("first_name","last_name","gender","email","age")
admin.site.register(Customer,CustomerAdmin)

# Register your models here.
