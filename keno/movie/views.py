from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer, MovieTitleSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class MovieModelViewSet(ModelViewSet):
    """
    ModelViewSet for getting, creating, updating and deleting movies.
    Endpoint: /api/v1/movies/
    """
    queryset = Movie.objects.all()
    http_method_names = ['get', 'post', 'delete']
    renderer_classes = [TemplateHTMLRenderer]

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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'movies': Movie.objects.all()}, template_name='movie/index.html')
