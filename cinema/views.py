from rest_framework import viewsets

from cinema.models import *


class CinemaHallViewSet(viewsets.ModelViewSet):
    model = CinemaHall
    