import json
from types import SimpleNamespace
from domain.ingredients.service import ServiceIngredient
from domain.ingredients.models.ingredient import Ingredient
from api.utils.response_generic import ResponseGeneric

class HandleIngredient:
    def __init__(self, request):
        self.request = request        
        self.service = ServiceIngredient()

    def get_ingredient(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def post_ingredient(self):
        ingredient = json.loads(self.request.data, object_hook=lambda d: Ingredient(**d))
        if type(ingredient) is not Ingredient:
            return ResponseGeneric('Bad Request!', 400)
            
        self.service.create_ingredient(ingredient)
        return ResponseGeneric('Still woozy ma friend', 200)

    def patch_ingredient(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def delete_ingredient(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def exec(self):
        if self.request.method == 'POST':
            return self.post_ingredient()
        elif self.request.method == 'GET':
            return self.get_ingredient()
        elif self.request.method == 'PATCH':
            return self.patch_ingredient()
        elif self.request.method == 'DELETE':
            return self.delete_ingredient()