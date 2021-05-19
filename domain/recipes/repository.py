from typing import Type
from bson.objectid import ObjectId
from domain.recipes.models.recipe import Recipe
from domain.config.database import database

class RepositoryRecipe:
    def __init__(self):
        self.database = database
        self.collection = self.database.db['recipes']

    def insert(self, recipe) -> bool:
        self.collection.insert(recipe.__dict__)
        return True
    
    def delete(self, id: str) -> bool:
        delete_result = self.collection.delete_one({'_id': ObjectId(id)})
        if delete_result.deleted_count < 1:
            return False
        return True
                

    def get_all(self) -> list:
        return list(self.collection.find({}))

    def update_recipe(self, recipe: Type[Recipe], id: str) -> bool:
        find = { "_id": ObjectId(id) }
        result = self.collection.update_one(find, { "$set": recipe.__dict__ })
        if result.modified_count < 1:
            return False
        return True