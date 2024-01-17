from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

user = "root"
password = "toor"
host = "mongo"


@app.route("/")
def main():
    client = connect(user, password, host)
    db = client.testdb

    return test_connection(db)


@app.route("/notes")
def show_notes():
    client = connect(user, password, host)
    db = client.testdb

    notes = [f"<p>{note['title']}</p>" for note in get_notes(db)]
    return "<h1>Notes</h1>" + "<br>".join(notes)


@app.route("/notes/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return """
        <h1>Create note</h1>
        <form action="/notes/create" method="post">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title">
            <br>
            <label for="content">Content:</label>
            <input type="text" id="content" name="content">
            <br>
            <label for="date">Date:</label>
            <input type="date" id="date" name="date">
            <br>
            <input type="submit" value="Submit">
        </form>
        """
    elif request.method == "POST":
        client = connect(user, password, host)
        db = client.testdb
        
        title = request.form["title"]
        content = request.form["content"]
        date = request.form["date"]
        note = Note(title, content, date)
        create_note(db, note)
        return f"Note created: {note.title}"


class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date


def connect(user, password, host, port=27017):
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def test_connection(db):
    try:
        db.command("serverStatus")
    except Exception:
        return "<h1>Connection failed</h1>"
    else:
        return "<h1>Connection successful</h1>"


def create_note(db, note):
    db.notes.insert_one(
        {"title": note.title, "content": note.content, "date": note.date}
    )


def get_notes(db):
    return db.notes.find()


def delete_note_by_title(db, title):
    db.notes.delete_one({"title": title})


def update_note_by_title(db, title, note):
    db.notes.update_one(
        {"title": title},
        {"$set": {"title": note.title, "content": note.content, "date": note.date}},
    )


if __name__ == "__main__":
    main()
