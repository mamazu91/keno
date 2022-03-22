from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.generics import CreateAPIView


#
# class MovieApiView(CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['post']
