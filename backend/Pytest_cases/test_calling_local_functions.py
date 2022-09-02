import requests
def test_add_table_message():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text': 'add_sheet("newguy", ["A", "B"], dataset=[["a", "b"]])'} ) # requesting with a incorrect url
    assert get_obj.status_code == 200
    dic = get_obj.json()
    assert dic['terminal'][1] == "success"

def test_drop_table_message():
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text': 'add_sheet("newguy", ["A", "B"], dataset=[["a", "b"]])'} ) # requesting with a incorrect url
    get_obj = requests.post("http://127.0.0.1:5000/scriptBox", json={'text': 'delete_sheet("newguy")'} )
    assert get_obj.status_code == 200
    dic = get_obj.json()
    assert dic['terminal'][1] == "success"