import bson.errors
import pymongo.errors
from bson.objectid import ObjectId
from pymongo import MongoClient


def connect(user, password, host, port=27017) -> MongoClient:
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def test_connection(db) -> str:
    try:
        db.command("serverStatus")
    except pymongo.errors.ConnectionFailure:
        return "failed: timeout"
    else:
        return "successful"


def create_note(db, note):
    return db.notes.insert_one(note).inserted_id


def find_notes(db):
    return db.notes.find()


def find_note(db, note_id):
    try:
        return db.notes.find_one({"_id": ObjectId(note_id)})
    except bson.errors.InvalidId:
        raise ValueError


def update_note(db, note_id, note):
    return db.notes.update_one({"_id": ObjectId(note_id)},
                               {"$set": note}).modified_count


def delete_notes(db):
    return db.notes.delete_many({}).deleted_count


def delete_note(db, note_id):
    return db.notes.delete_one({"_id": ObjectId(note_id)}).deleted_count
