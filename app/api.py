from flask import Flask, jsonify, request

import models
import db_manager as dbm

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

user = "root"
password = "toor"
host = "mongo"


@app.route("/")
def main():
    client = dbm.connect(user, password, host)
    db = client.testdb

    return {"status": dbm.test_connection(db)}


@app.route("/notes", methods=["GET"])
def find_notes():
    client = dbm.connect(user, password, host)
    db = client.testdb

    notes = dbm.find_notes(db)

    return jsonify({"notes": notes})


@app.route("/notes", methods=["POST"])
def create_note():
    client = dbm.connect(user, password, host)
    db = client.testdb

    note = request.json

    note_id = dbm.create_note(db, note)
    return jsonify({"note_id": str(note_id)})


@app.route("/notes", methods=["DELETE"])
def delete_notes():
    client = dbm.connect(user, password, host)
    db = client.testdb

    dbm.delete_notes(db)

    return jsonify({"status": "success"})


@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    client = dbm.connect(user, password, host)
    db = client.testdb

    dbm.delete_note(db, note_id)

    return jsonify({"status": "success"})
