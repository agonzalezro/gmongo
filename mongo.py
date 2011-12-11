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

    def _get_database(self, database):
        return getattr(self.connection, database)

    def _get_collection(self, database, collection):
        return getattr(self._get_database(database), collection)

    def get_all_databases(self):
        return self.connection.database_names()

    def get_all_collections(self, database):
        database = getattr(self.connection, database)
        return database.collection_names()

    def get_all_documents(self, database, collection):
        database = getattr(self.connection, database)
        collection = getattr(database, collection)
        return collection.find()

    def get_content(self, database, collection, filter):
        collection = self._get_collection(database, collection)
        key = collection.find()[0].keys()[0]
        return collection.find({key: filter})[0]

    def get_count(self, database, collection=None):
        database = getattr(self.connection, database)
        if collection:
            return getattr(database, collection).count()
        return len(database.collection_names())
