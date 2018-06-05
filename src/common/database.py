import pymongo

__author__ = "roberto munoz garcia"


class Database(object):
    URI = "mongodb://<ekpro>:<ekpro123>@ds247330.mlab.com:47330/heroku_7p7jgn5l"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_database()
