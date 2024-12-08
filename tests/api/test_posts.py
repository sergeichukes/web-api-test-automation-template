import requests
from tests.conftest import API_URL
import http.client
from models.api_models import BlogPost, BlogPostResponse


http.client.HTTPConnection.debuglevel = 1

def test_success_get_all_posts():
    # Arrange

    # Act
    response = requests.get(f"{API_URL}/posts")

    # Assert
    assert "posts" in response.json(), 'Could not find "post" in the response'
    assert response.status_code == 200, 'Incorrect status code'

def test_success_get_post():
    # Arrange
    response: BlogPostResponse = requests.get(f"{API_URL}/posts").json()

    posts = [BlogPost.model_validate(item) for item in response['posts']]
    expected_post = posts[0]

    # Act
    post_response = BlogPost.model_validate(requests.get(f"{API_URL}/posts/{expected_post.id}").json())

    # Assert
    assert expected_post == post_response, "Posts are different"
