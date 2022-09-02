import requests
def test_console_message():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text': 'print("testing console message")'} ) # requesting with a incorrect url
    assert get_obj.status_code == 200
    dic = get_obj.json()
    assert dic['terminal'][1] == "success"
    assert dic['terminal'][0] == 'testing console message\n'

def test_not_stdout():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text':'a = 1 + 1'} ) # requesting with a incorrect url
    assert get_obj.status_code == 200
    dic = get_obj.json()
    assert dic['terminal'][1] == "success"
    assert dic['terminal'][0] == ''