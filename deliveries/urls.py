
from django.urls import path
from .views import product_delivery_view


urlpatterns = [
    path("deliveries/upload/",product_delivery_view,name = "product_delivery_views"),

]