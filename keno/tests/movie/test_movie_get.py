import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_movie_list(api_client, movie_factory):
    """
    The test for getting the list of all movies.
    """
    movies = movie_factory(_quantity=2)
    url = reverse('movie_add-list')
    response = api_client.get(url)
    assert response.status_code == 200

    # Not sure how optimal is this. The idea is to check that all existing movies are returned,
    # but as movies and response.data are of different types (Movie object vs list of OrderedDicts),
    # you cannot compare them easily.
    assert sorted([movie.title for movie in movies]) == sorted([movie.get('title') for movie in response.data])


@pytest.mark.django_db
def test_movie_retrieve(api_client, movie_factory):
    """
    The test for retrieving a movie.
    """
    movie = movie_factory()
    url = reverse('movie_add-list')
    response = api_client.get(url)
    assert response.status_code == 200

    # Even though retrieve is always going to return only 1 item, the item is going to be in a list.
    assert response.data.pop().get('title') == movie.title
