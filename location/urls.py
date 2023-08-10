from django.urls import path
from .views import location_upload_view
from .views import location_update_view


urlpatterns = [
    path("location/upload/",location_upload_view,name = "location_upload_views"),

    path("location/edit/<int:id>/",location_update_view,name="location_update_view"),

]






