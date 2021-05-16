from typing import Type
from bson.objectid import ObjectId
from domain.cakes.models.cake import Cake
from domain.config.database import database

class RepositoryCake:
    def __init__(self):
        self.database = database
        self.collection = self.database.db['cakes']

    def insert(self, cake):
        self.collection.insert(cake.__dict__)
        return True
    
    def delete(self, id: str):
        delete_result = self.collection.delete_one({'_id': ObjectId(id)})
        if delete_result.deleted_count < 1:
            return False
        return True
                

    def get_all(self):
        return list(self.collection.find({}))

    def update_cake(self, cake: Type[Cake], id: str):
        find = { "_id": ObjectId(id) }
        result = self.collection.update_one(find, { "$set": cake.__dict__ })
        if result.modified_count < 1:
            return False
        return True