from flask import Flask, request

app = Flask(__name__)

notes = []


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/delete_all', methods=['DELETE'])
def get_note_by_id():
    global notes
    notes = []
    return notes

@app.route('/notes', methods=['POST', 'GET', 'PUT', 'DELETE'])
def do_notes():
    global notes
    if request.method == "GET":
        id = request.json['id']
        return list(filter(lambda x: x['id'] == id, notes))
    elif request.method == "POST":
        data = request.json
        if len(data) > 0:
            for i in data:
                notes.append(i)
        return notes
    elif request.method == "DELETE":
        id = request.json['id']
        notes = list(filter(lambda x: x['id'] != id, notes))
        return notes
    elif request.method == "PUT":
        id = request.json['id']
        text = request.json['text']
        notes_found = list(filter(lambda x: x['id'] == id, notes))
        notes = list(filter(lambda x: x['id'] != id, notes))
        for note in notes_found:
            notes.append({"id":id, "text":text, "time":note["time"]})
        return notes