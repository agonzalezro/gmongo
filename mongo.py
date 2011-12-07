import pymongo

class Mongo():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = (super(Mongo, cls).
                                __new__(cls, *args, **kwargs))
        return cls._instance

    def __init__(self):
        self.connection = pymongo.Connection()

    def get_all_databases(self):
        return self.connection.database_names()

    def get_all_documents(self, database):
        database = getattr(self.connection, database)
        return database.collection_names()

    def get_count(self, database, document=None):
        database = getattr(self.connection, database)
        if document:
            return getattr(database, document).count()
        return len(database.collection_names())
