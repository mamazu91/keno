import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_movie_add(api_client, movie_factory):
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
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    assert response.data == payload


@pytest.mark.django_db
def test_movie_add_with_empty_payload(api_client):
    payload = {}
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_with_no_title(api_client):
    payload = {
        "movies": []
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_with_empty_title(api_client):
    payload = {
        "movies": [
            {

            }
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_with_wrong_title(api_client):
    payload = {
        "movies": [
            {
                "wrong_title": "movie"
            }
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_with_empty_title(api_client):
    payload = {
        "movies": [
            {
                "title": ''
            }
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_with_too_long_title(api_client):
    payload = {
        "movies": [
            {
                "title": 256 * "a"
            }
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_existing_title(api_client, movie_factory):
    movie = movie_factory()
    payload = {
        "movies": [
            {
                "title": movie.title
            },
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_movie_add_same_titles(api_client):
    payload = {
        "movies": [
            {
                "title": "movie"
            },
            {
                "title": "movie"
            }
        ]
    }
    url = reverse('movie_add-list')
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    assert len(response.data['movies']) == 1
