import requests

def test_404():
    get_obj = requests.post("http://127.0.0.1:5000/random_request", "random data") # requesting with a incorrect url
    assert get_obj.status_code == 404
    assert get_obj.text == "<h1>404</h1><p>The resource could not be found.</p>"