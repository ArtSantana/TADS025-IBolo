from decouple import config
from pymongo import MongoClient

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')

client = MongoClient('mongodb://%s:%s@127.0.0.1' % (DB_USER, DB_PASSWORD), 27017)