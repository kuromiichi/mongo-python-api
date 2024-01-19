import uuid
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

user = "root"
password = "toor"
host = "mongo"


@app.route("/")
def main():
    client = connect(user, password, host)
    db = client.testdb

    return render_template("index.html", status=test_connection(db))


@app.route("/notes")
def show_notes():
    client = connect(user, password, host)
    db = client.testdb

    return render_template("notes.html", notes=get_notes(db))


@app.route("/notes/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create_note.html")
    elif request.method == "POST":
        client = connect(user, password, host)
        db = client.testdb

        title = request.form["title"]
        content = request.form["content"]
        date = request.form["date"]

        if (not title) or (not content) or (not date):
            return render_template("create_note.html")

        note = Note(title, content, date)
        create_note(db, note)
        return render_template("note_created.html", note=note)


@app.route("/notes/delete", methods=["POST"])
def delete():
    uuid = request.form["uuid"]

    client = connect(user, password, host)
    db = client.testdb

    delete_note(db, uuid)

    return render_template("notes.html", notes=get_notes(db))


class Note:
    def __init__(self, title, content, date):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.date = date


def connect(user, password, host, port=27017):
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def test_connection(db):
    try:
        db.command("serverStatus")
    except Exception:
        return "failed"
    else:
        return "successful"


def create_note(db, note):
    db.notes.insert_one(
        {
            "uuid": note.uuid,
            "title": note.title,
            "content": note.content,
            "date": note.date,
        }
    )


def get_notes(db):
    return db.notes.find()


def delete_note(db, uuid):
    db.notes.delete_one({"uuid": uuid})


def delete_note_by_title(db, title):
    db.notes.delete_one({"title": title})


def update_note_by_title(db, title, note):
    db.notes.update_one(
        {"title": title},
        {"$set": {"title": note.title, "content": note.content, "date": note.date}},
    )


if __name__ == "__main__":
    main()
