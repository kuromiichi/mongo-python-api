import bson.errors
import pymongo.errors
from bson.objectid import ObjectId
from pymongo import MongoClient


# Connect to MongoDB
def connect(user, password, host, port=27017) -> MongoClient:
    return MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


# Test connection
def test_connection(db) -> str:
    try:
        db.command("serverStatus")
    except pymongo.errors.ConnectionFailure:
        return "failed: timeout"
    else:
        return "successful"


# Create note
def create_note(db, note):
    return db.notes.insert_one(note).inserted_id


# Find all notes
def find_notes(db):
    return db.notes.find()


# Find one note
def find_note(db, note_id):
    try:
        return db.notes.find_one({"_id": ObjectId(note_id)})
    except bson.errors.InvalidId:
        raise ValueError


# Update note
def update_note(db, note_id, note):
    return db.notes.update_one({"_id": ObjectId(note_id)},
                               {"$set": note}).modified_count


# Delete all notes
def delete_notes(db):
    return db.notes.delete_many({}).deleted_count


# Delete one note
def delete_note(db, note_id):
    return db.notes.delete_one({"_id": ObjectId(note_id)}).deleted_count
