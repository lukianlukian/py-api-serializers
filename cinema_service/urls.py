from django.contrib import admin
from django.urls import path
from cinema.views import (
    CinemaHallViewSet,
    )


urlpatterns = [
    path("admin/", admin.site.urls),
]
