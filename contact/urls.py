from django.urls import path
from .views import contact_upload_view


urlpatterns = [
    path("contact/upload/",contact_upload_view,name = "contact_upload_views"),

]