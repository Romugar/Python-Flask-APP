import pymongo

__author__ = "roberto munoz garcia"


class Database(object):
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient("aqui la direccion de la BBDD mongoDB")
        Database.DATABASE = client["aqui el nombre de la BBDD"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, id, query):
        return Database.DATABASE[collection].update(id, query)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
