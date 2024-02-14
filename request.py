import requests

url = "http://localhost:5000/notes"
headers = {"Content-Type": "application/json"}

note = {
    "title": "título de prueba",
    "date": "2020-01-01",
    "is_done": False,
    "type": "TEXT",
    "content": "esto es un contenido de prueba"
}


def test_create_note():
    response = requests.post(url, headers=headers, json=note)
    print(response.json())


def delete_notes():
    response = requests.delete(url)
    print(response.json())


def delete_one_note(note_id):
    response = requests.delete(url + "/" + note_id)
    print(response.json())


if __name__ == "__main__":
    delete_one_note("65b0340dcac61a479d9b3ce7")
