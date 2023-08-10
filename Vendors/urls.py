from django.urls import path
from .views import Vendor_form_view


urlpatterns = [
    path("Vendors/upload/",Vendor_form_view ,name = "vendor_upload_views"),

]
