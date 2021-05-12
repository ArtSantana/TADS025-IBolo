import json
from types import SimpleNamespace
from domain.recipes.service import ServiceRecipes
from domain.recipes.models.recipe import Recipe
from api.utils.response_generic import ResponseGeneric

class HandleRecipes:
    def __init__(self, request):
        self.request = request        
        self.service = ServiceRecipes()

    def get_recipes(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def post_recipe(self):
        recipe = json.loads(self.request.data, object_hook=lambda d: Recipe(**d))
        if type(recipe) is not Recipe:
            return ResponseGeneric('Bad Request!', 400)
            
        self.service.create_recipe(recipe)
        return ResponseGeneric('Still woozy ma friend', 200)

    def patch_recipe(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def delete_recipe(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def exec(self):
        if self.request.method == 'POST':
            return self.post_recipe()
        elif self.request.method == 'GET':
            return self.get_recipest()
        elif self.request.method == 'PATCH':
            return self.patch_recipe()
        elif self.request.method == 'DELETE':
            return self.delete_recipe()