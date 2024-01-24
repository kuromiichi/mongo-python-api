from flask import Flask, jsonify, request

import db_manager as dbm

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

user = "root"
password = "toor"
host = "mongo"


@app.route("/")
def main():
    db = dbm.connect(user, password, host).testdb

    return jsonify({"status": dbm.test_connection(db)})


@app.route("/notes", methods=["GET"])
def find_notes():
    db = dbm.connect(user, password, host).testdb

    notes = {str(note.pop("_id")): note for note in list(dbm.find_notes(db))}
    return jsonify({"notes": notes})


@app.route("/notes/<note_id>", methods=["GET"])
def find_note(note_id):
    db = dbm.connect(user, password, host).testdb

    try:
        note = dbm.find_note(db, note_id)
    except ValueError:
        return jsonify({"error": "Invalid note ID"})

    note = {str(note.pop("_id")): note} if note else "not found"
    return jsonify({"note": note})


@app.route("/notes", methods=["POST"])
def create_note():
    db = dbm.connect(user, password, host).testdb

    note = request.json

    note_id = dbm.create_note(db, note)
    return jsonify({"note_id": str(note_id)})


@app.route("/notes/<note_id>", methods=["PUT"])
def update_note(note_id):
    db = dbm.connect(user, password, host).testdb

    note = request.json
    modified_count = dbm.update_note(db, note_id, note)
    return jsonify({"updated": True if modified_count else False})


@app.route("/notes", methods=["DELETE"])
def delete_notes():
    db = dbm.connect(user, password, host).testdb

    deleted_count = dbm.delete_notes(db)
    return jsonify({"deleted": deleted_count})


@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    db = dbm.connect(user, password, host).testdb

    deleted_count = dbm.delete_note(db, note_id)
    return jsonify({"deleted": True if deleted_count else False})
