import pymongo

__author__ = "roberto munoz garcia"


class Database(object):
    URI = "mongodb://ekpro:ekpro123@ds247330.mlab.com:47330/heroku_7p7jgn5l"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient("mongodb://ekpro:ekpro123@ds247330.mlab.com:47330/heroku_7p7jgn5l")
        Database.DATABASE = client["heroku_7p7jgn5l"]

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
