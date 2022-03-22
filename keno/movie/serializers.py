from rest_framework.serializers import ModelSerializer
from .models import Movie
from .utils import get_unique_movie_titles


class MovieTitleSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']


class MovieSerializer(ModelSerializer):
    movies = MovieTitleSerializer(many=True, allow_empty=False)

    class Meta:
        model = Movie
        fields = ['movies']

    def create(self, validated_data):
        """
        Not sure if this code is optimal. The idea was to use bulk_create specifically,
        plus return only those movies that were inserted into the DB.
        But even with ignore_conflicts bulk_create returns a list of both created and not created movies.
        So the best solution seemed to be to get rid of the duplicates beforehand.
        Solution was taken from here:
        https://gist.github.com/bityob/7a4e00946c6226e4a7d26bb6a429fb3a?short_path=ac216bb.

        I also don't really like how return {'movies': movies} looks like,
        but to my surprise I wasn't able to find anything more elegant.
        """
        unique_titles = get_unique_movie_titles(validated_data.pop('movies'))

        # Movie(**movie) is a really cool to create unhashable objects (objects with no pk). Found it here:
        # https://www.django-rest-framework.org/api-guide/serializers/#customizing-multiple-create
        unique_titles_objects = [Movie(**movie) for movie in unique_titles]

        movies = Movie.objects.bulk_create(unique_titles_objects, ignore_conflicts=True)
        return {'movies': movies}
