from django.contrib import admin

from .models import Contact
class ContactAdmin (admin.ModelAdmin):
    total_display = ("phone_number"," email","address","social_medias")
admin.site.register(Contact,ContactAdmin)

# Register your models here.
