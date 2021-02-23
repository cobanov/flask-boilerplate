import pymongo
from datetime import datetime

DB_NAME = "test"
COLLECTION = "entries"


def connect_db(db_name=DB_NAME):
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client[db_name]

    print("DB List:", client.list_database_names())
    return db


def write_data(db, collection):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    entry = {"time": current_time, "message": "hello world!",
             "message_id": 1, "author": "Cobanov"}
    db[collection].insert_one(entry)


def retrieve_data(db, collection):
    data = db[collection].find()
    return data
