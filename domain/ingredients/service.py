from domain.ingredients.models.ingredient import Ingredient
from typing import Type, TypeVar

class ServiceIngredient:
    def create_ingredient(self, ingredient: Type[Ingredient]):
        print(ingredient.name, ingredient.unit, ingredient.price)
    
    def get_ingredients(self):
        print('getting ingredients')
    
    def delete_ingredients(self, id: str):
        print(id)

    def update_ingredients(self, ingredient: Type[Ingredient]):
        print(ingredient)