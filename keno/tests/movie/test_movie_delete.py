import pytest
from django.urls import reverse
import random


@pytest.mark.django_db
def test_movie_delete(api_client, movie_factory):
    """
    The test for deleting a movie by its id.
    """
    movies = movie_factory(_quantity=3)
    random_movie = random.choice(movies)
    url = reverse('movies-detail', args=(random_movie.id,))
    response = api_client.delete(url)
    assert response.status_code == 204

    # Ensuring the movie no longer exists in the DB.
    url = reverse('movies-detail', args=(random_movie.id,))
    response = api_client.get(url)
    assert response.status_code == 404

    # Ensuring the DB has the same amount of movies minus the amount of deleted movies.
    url = reverse('movies-list')
    response = api_client.get(url)
    assert len(response.data) == len(movies) - 1
