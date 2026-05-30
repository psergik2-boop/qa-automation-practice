import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_status_code():
    """Check that GET request returns 200 OK"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_get_post_content():
    """Check that response contains expected fields"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data
    assert "body" in data
    assert data["userId"] == 1


def test_create_post():
    """Check creating a new post via POST request"""
    new_post = {"title": "Test", "body": "Test body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "Test"
