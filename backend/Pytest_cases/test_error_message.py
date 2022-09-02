import requests
def test_error_message():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text': 'a = b * 1'} ) # requesting with a incorrect url
    assert get_obj.status_code == 200
    dic = get_obj.json()
    assert dic['terminal'][1] == "exception"
