import pymongo

class Database:
    DB=None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.db = client.mydb

    @staticmethod
    def insert_record(doc):
        Database.db.usercol.insert_one(doc)

    @staticmethod
    def get_records():
        records=[doc for doc in Database.db.usercol.find({})]
        return records

    @staticmethod
    def delete_all():
        Database.db.usercol.drop()

    @staticmethod
    def delete_one(doc):
        Database.db.usercol.delete_one(doc)

    @staticmethod
    def update_one(arg,doc):
        Database.db.usercol.update(arg,doc)