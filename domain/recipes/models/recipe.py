from types import SimpleNamespace
from bson.objectid import ObjectId
from domain.ingredients.models.ingredient import Ingredient


class Recipe:
    def __init__(self,):
        self.__ingredients = []
        self.__name = ''

    def setIngredients(self, ingredients):
        self.__ingredients = ingredients

    def setName(self, name):
        self.__name = name

    def getIngredients(self):
        return self.__ingredients

    def getName(self):
        return self.__name

    def parseFromRequest(self, r: SimpleNamespace):
        self.__name = r.name
        new_items = []
        for document in r.ingredients:
            ingredient = {
                "id": document.ingredient.id,
                "name": document.ingredient.name,
                "price": document.ingredient.price,
                "unit": document.ingredient.unit 
            }
            quantity = document.quantity
            new_items.append({'ingredient': ingredient, 'quantity': quantity})
        self.__ingredients = new_items