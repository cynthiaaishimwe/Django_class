from django.urls import path
from .views import payment_form_view


urlpatterns = [
    path("payments/upload/",payment_form_view ,name = "payment_upload_views"),

]