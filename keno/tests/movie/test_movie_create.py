import pytest
from django.urls import reverse

"""
Don't really like writing payload manually here -- seems like there might be a better solution --,
but couldn't come up with a better one. Tried to create movies with movie_factory,
then serializer them into a dict, but that didn't work well, as I was getting an error on making the POST request.
"""


@pytest.mark.django_db
def test_movie_create(api_client):
    """
    The only test with proper inputs.
    Not sure if the naming is good, but couldn't come up with something better.
    """
    payload = {
        "movies": [
            {
                "title": "movie1"
            },
            {
                "title": "movie2"
            }
        ]
    }
    url = reverse('movies-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    assert response.data == payload


@pytest.mark.parametrize(
    ['payload', 'expected_status'],
    (
            ({}, 400),
            ({'movies': []}, 400),
            ({'movies': [{}]}, 400)
    )
)
@pytest.mark.django_db
def test_movie_create_with_empty_payload(api_client, payload, expected_status):
    """
    The test for all different kinds of empty payload.
    """
    url = reverse('movies-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ['payload', 'expected_status'],
    (
            ({'movies': [{'wrong_title': 'movie'}]}, 400),
            ({'movies': [{'title': ''}]}, 400),
            ({'movies': [{'title': 256 * 'a'}]}, 400)
    )
)
@pytest.mark.django_db
def test_movie_create_with_bad_title(api_client, payload, expected_status):
    """
    The test for all different kinds of bad title.
    Not sure how obvious is 256 * 'a', but the idea was to show that title has max_length=255.
    """
    url = reverse('movies-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == expected_status


@pytest.mark.django_db
def test_movie_create_with_existing_title(api_client, movie_factory):
    """
    The test to check that if a movie exists,
    another one with the same title is not going to be created.
    """
    existing_movie = movie_factory()
    payload = {
        'movies': [
            {
                'title': existing_movie.title
            },
        ]
    }
    url = reverse('movies-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_create_with_same_title_twice(api_client):
    """
    The test to check that the same movie cannot be created twice.
    Also checks that the response is not going to contain any duplicates.
    """
    payload = {
        'movies': [
            {
                'title': 'movie'
            },
            {
                'title': 'movie'
            }
        ]
    }
    url = reverse('movies-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    assert len(response.data['movies']) == 1
