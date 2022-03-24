from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer, MovieTitleSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status


class HomeApiView(APIView):
    """
    APIView that returns HTML containing table with list of all movies.
    Endpoint: /
    """
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        """
        Created the function just in case I need to add some more logic to making of the resulting queryset.
        By default, APIView doesn't implement get_queryset function, so it's not an override per se.
        """
        return Movie.objects.all()

    def get(self, request):
        """
        Not sure why, but even though PyCharm does not automatically add request parameter
        when creating the function, it's not going to work without it. Weird.
        """
        return Response({'movies': self.get_queryset()}, template_name='movie/index.html', status=status.HTTP_200_OK)


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
