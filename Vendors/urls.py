from django.urls import path
from . import views
from .views import vendor_display
from .views import vendor_detail
from .views import vendor_upload_view


app_name = 'vendors'


urlpatterns = [
    path('vendors/list/', vendor_display, name='vendor_display'),
    path('vendors/<int:id>/',vendor_detail, name='vendor_detail'),
    path('vendors/upload/', vendor_upload_view, name='vendor_form'),
    
]

