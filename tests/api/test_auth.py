import requests
from tests.conftest import API_URL
import http.client

http.client.HTTPConnection.debuglevel = 1

def test_login_api():
    # https://jsonplaceholder.typicode.com/
    response = requests.get(f"{API_URL}/posts")
    assert "posts" in response.json(), 'Pupupuuu'
    assert response.status_code == 200
