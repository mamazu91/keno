from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer, MovieTitleSerializer


class MovieModelViewSet(ModelViewSet):
    """
    ModelViewSet for getting, creating, updating and deleting movies.
    Endpoint: /api/v1/movies/
    """
    queryset = Movie.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def get_serializer_class(self):
        """
        Override because GET and POST require different serializers.
        """
        if self.action == 'retrieve':
            return MovieTitleSerializer
        elif self.action == 'list':
            return MovieTitleSerializer
        elif self.action == 'create':
            return MovieSerializer
