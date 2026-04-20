from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

class ActorSerializer(serializers.ModelSerializer):
    # SerializerMethodField - field that calculates by function
    full_name = serializers.SerializerMethodField()

    class Meta:
        query_set = Actor.objects.all()
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj: Actor) -> str:
        # obj — certain field Actor from database
        return f"{obj.first_name} {obj.last_name}"

class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        query_set = CinemaHall.objects.all()
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

class MovieListSerializer(serializers.ModelSerializer):
    # SlugRelatedField — shows related objects through one their field
    # slug_field - what field Genre should show
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField(

    )
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, obj: Movie) -> list:
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionListSerializer(serializers.ModelSerializer):
    """GET /api/cinema/movie_sessions/"""

    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    """GET /api/cinema/movie_sessions/<pk>/ """

    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionWriteSerializer(serializers.ModelSerializer):
    """POST / PUT """

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
