from decouple import config
from pymongo import MongoClient

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')
CONNECTION_URI = 'mongodb://%s:%s@127.0.0.1' % (DB_USER, DB_PASSWORD)

class DatabaseControl:
    def __init__(self):
        self.client = MongoClient(CONNECTION_URI, 27017)
        self.db = self.client[DB_NAME]

    def close_connection(self):
        self.client.close()
    
database = DatabaseControl()