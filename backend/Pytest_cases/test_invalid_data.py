import requests
def test_no_body():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox") # requesting with a incorrect url
    assert get_obj.status_code == 415

def test_not_json():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", data = "not json") # requesting with a incorrect url
    assert get_obj.status_code == 415

def test_invalid_key():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'invalid_key': 'a = 1 * 1'}) # requesting with a incorrect url
    assert get_obj.status_code == 415