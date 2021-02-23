import pymongo
from datetime import datetime

DB_NAME = "test"
COLLECTION = "entries"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def connect_db(db_name=DB_NAME):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]

    print("DB List:", client.list_database_names())
    return db


def write_data(db, collection, entry):
    db[collection].insert_one(entry)


def retrieve_data(db, collection):
    data = db[collection].find()
    return data


# mydb = connect_db(DB_NAME)

# entry_first = {"time": current_time, "message": "hello world!",
#                "message_id": 1, "author": "Cobanov"}

# write_data(mydb, "entries", entry_first)


#entries_db = mydb["entries"]
