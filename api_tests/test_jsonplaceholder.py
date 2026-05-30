"""
API tests for JSONPlaceholder.
Free online REST API for testing and prototyping.
https://jsonplaceholder.typicode.com
"""

import requests


def test_get_post_status_code(api_base_url):
    """GET request should return status 200."""
    response = requests.get(f"{api_base_url}/posts/1")
    assert response.status_code == 200


def test_get_post_has_required_fields(api_base_url):
    """Response should contain title, body and userId fields."""
    response = requests.get(f"{api_base_url}/posts/1")
    data = response.json()

    assert "title" in data
    assert "body" in data
    assert "userId" in data
    assert isinstance(data["userId"], int)   # не хардкодим == 1


def test_create_new_post(api_base_url):
    """POST request should create a new post and return status 201."""
    new_post = {
        "title": "My test post",
        "body": "This is a sample body",
        "userId": 1,
    }
    response = requests.post(f"{api_base_url}/posts", json=new_post)

    assert response.status_code == 201
    assert response.json()["title"] == new_post["title"]


def test_delete_post(api_base_url):
    """DELETE request should return status 200."""
    response = requests.delete(f"{api_base_url}/posts/1")
    assert response.status_code == 200
