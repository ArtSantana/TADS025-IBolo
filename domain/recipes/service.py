from types import SimpleNamespace
from domain.recipes.models.recipe import Recipe
from domain.recipes.models.recipe_db import RecipeDB
from domain.recipes.repository import RepositoryRecipe
from typing import Type

class ServiceRecipe:
    def __init__(self):
        self.repository = RepositoryRecipe()

    def create_recipe(self, recipe: SimpleNamespace):
        return self.repository.insert(recipe)
    
    def get_all_recipes(self):
        list = self.repository.get_all()
        obj_list = []
        for document in list:
            parsed_recipe = RecipeDB()
            parsed_recipe.parseFromDict(document)
            obj_list.append(parsed_recipe.__dict__)
        return obj_list

    
    def delete_recipe(self, id: str):
        return self.repository.delete(id)

    def update_recipes(self, recipe: Type[Recipe], id: str):
        return self.repository.update_recipe(recipe, id)