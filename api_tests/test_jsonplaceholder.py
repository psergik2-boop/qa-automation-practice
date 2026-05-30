"""
API tests for JSONPlaceholder
A fake online REST API for testing and prototyping.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_status_code():
    """GET request should return status code 200"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_get_post_has_required_fields():
    """Response should contain title, body and userId"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data
    assert "body" in data
    assert data["userId"] == 1


def test_create_new_post():
    """POST request should create a new post and return 201"""
    new_post = {
        "title": "My test post",
        "body": "This is a test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "My test post"


def test_delete_post():
    """DELETE request should return status code 200"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
