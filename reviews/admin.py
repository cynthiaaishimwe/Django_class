from django.contrib import admin

from .models import Reviews
class ReviewsAdmin (admin.ModelAdmin):
    total_display = ("email","comment")
admin.site.register(Reviews,ReviewsAdmin)



# Register your models here.
