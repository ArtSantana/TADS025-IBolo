from domain.ingredients.models.ingredient import Ingredient
from domain.ingredients.models.ingredient_db import IngredientDB
from domain.ingredients.repository import RepositoryIngredient
from typing import Type

class ServiceIngredient:
    def __init__(self):
        self.repository = RepositoryIngredient()

    def create_ingredient(self, ingredient: Type[Ingredient]):
        return self.repository.insert(ingredient)
    
    def get_all_ingredients(self):
        list = self.repository.get_all()
        obj_list = []
        for document in list:
            parsed_ingredient = IngredientDB()
            parsed_ingredient.parseFromDict(document)
            obj_list.append(parsed_ingredient.__dict__)
        return obj_list

    
    def delete_ingredient(self, id: str):
        return self.repository.delete(id)

    def update_ingredients(self, ingredient: Type[Ingredient], id: str):
        return self.repository.update_ingrendient(ingredient, id)