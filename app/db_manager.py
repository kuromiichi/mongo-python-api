from collections import OrderedDict

from pymongo import MongoClient


def connect(user, password, host, port=27017) -> MongoClient:
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def test_connection(db) -> str:
    try:
        db.command("serverStatus")
    except Exception:
        return "failed"
    else:
        return "successful"


def create_note(db, note):
    return db.notes.insert_one(note).inserted_id


def find_notes(db):
    return {str(note.pop("_id")): note for note in list(db.notes.find())}


def update_note(db, note_id, note):
    return db.notes.update_one({"_id": note_id}, {"$set": note})


def delete_notes(db):
    return db.notes.delete_many({})


def delete_note(db, note_id):
    return db.notes.delete_one({"_id": note_id})
