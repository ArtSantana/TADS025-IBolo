from typing import Type
from bson.objectid import ObjectId
from domain.ingredients.models.ingredient import Ingredient
from domain.config.database import database

class RepositoryIngredient:
    def __init__(self):
        self.database = database
        self.collection = self.database.db['ingredients']

    def insert(self, ingredient: Type[Ingredient]):
        try:
            result = self.collection.insert(ingredient.__dict__)
            return True
        except:
            return False
    
    def delete(self, id: str):
        delete_result = self.collection.delete_one({'_id': ObjectId(id)})
        if delete_result.deleted_count < 1:
            return False
        return True
                

    def get_all(self):
        return list(self.collection.find({}))

    def update_ingrendient(self, ingredient: Type[Ingredient], id: str):
        find = { "_id": ObjectId(id) }
        result = self.collection.update_one(find, { "$set": ingredient.__dict__ })
        if result.modified_count < 1:
            return False
        return True
