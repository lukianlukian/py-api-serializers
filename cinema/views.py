from rest_framework import viewsets

from cinema.models import *


class CinemaHallViewSet(viewsets.ModelViewSet):
    model = CinemaHall


class ActorViewSet(viewsets.ModelViewSet):
    model = CinemaHall


class GenreViewSet(viewsets.ModelViewSet):
    model = CinemaHall


class MovieViewSet(viewsets.ModelViewSet):
    model = CinemaHall


# asdlasd alsdpa d