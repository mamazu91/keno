from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer


class MovieModelViewSet(ModelViewSet):
    """
    ModelViewSet for creating movies.
    Endpoint: /api/v1/movies/
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['post']
