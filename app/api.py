from pymongo import MongoClient


def main():
    user = "root"
    password = "toor"
    host = "mongodb"

    client = connect(user, password, host)
    db = client.testdb
    test_connection(db)

    print("init")
    for note in get_notes(db):
        print(note)

    create_note(db, Note("title", "content", "date"))

    print("after insert")
    for note in get_notes(db):
        print(note)

    update_note_by_title(db, "title", Note("new title", "new content", "new date"))

    print("after update")
    for note in get_notes(db):
        print(note)

    delete_note_by_title(db, "new title")

    print("after delete")
    for note in get_notes(db):
        print(note)


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
        print("Connection failed")
    else:
        print("Connection successful")


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
