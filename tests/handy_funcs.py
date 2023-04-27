import requests

def add_note(note, id=1):
    url = "http://127.0.0.1:5000/notes"

    payload = [{
    "text": note,
    "time": "Wed, 21 Oct 2015 18:27:50 GMT",
    "id" : id
    }]
    requests.post(url, json=payload)

def get_note(id):
    url = "http://127.0.0.1:5000/notes"

    payload = {"id" : id}
    res = requests.get(url, json=payload)
    if len(res.json()) > 0 :
        return res.json()[0]['text']
    return None

def modify_note(note, id):
    url = "http://127.0.0.1:5000/notes"

    payload = {
    "text": note,
    "id" : id
    }
    requests.put(url, json=payload) 

def delete_note(id):
    url = "http://127.0.0.1:5000/notes"

    payload = {
    "id" : id
    }
    requests.delete(url, json=payload) 

def clear_notes():
    url = "http://127.0.0.1:5000/delete_all"
    requests.delete(url) 