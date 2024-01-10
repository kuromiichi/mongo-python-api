import pymongo


def connect(user, password, host):
    return pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:27017/")


def test_connection(db):
    try:
        db.command("serverStatus")
    except Exception:
        print("Connection failed")
    else:
        print("Connection successful")


user = "root"
password = "toor"
host = "mongodb"

client = connect(user, password, host)
test_connection(client.testdb)
