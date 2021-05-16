import json
from types import SimpleNamespace
from domain.recipes.service import ServiceRecipe
from domain.recipes.models.recipe import Recipe
from api.utils.response_generic import ResponseGeneric

class HandleRecipe:
    def __init__(self, request):
        self.request = request        
        self.service = ServiceRecipe()

    def get_recipes(self):
        items = self.service.get_all_recipes()
        response = ResponseGeneric()
        response.data.items = items
        return response

    def post_recipe(self):
        response = ResponseGeneric()
        recipe_request = json.loads(self.request.data, object_hook=lambda d: SimpleNamespace(**d))
        recipe = Recipe()
        try:
            recipe.parseFromRequest(recipe_request)
        except:
            response.status = 400
            response.message = 'Bad request!'
        if self.service.create_recipe(recipe):
            response.status = 201
            response.message = 'Created!'
        else:
            response.status = 500
            response.message = 'Internal server error!'
        return response

    def put_recipe(self, id: str):
        response = ResponseGeneric()
        recipe_request = json.loads(self.request.data, object_hook=lambda d: SimpleNamespace(**d))
        recipe = Recipe()
        recipe.parseFromRequest(recipe_request)
        if self.service.update_recipes(recipe, id):
            response.message = 'Success'
            response.status = 200
        else:
            response.message = 'Internal server error!'
            response.status = 500
        return response

    def delete_recipe(self, id: str):
        response = ResponseGeneric()
        if len(id) < 1:
            response.status = 400
            response.data.message = 'Required id value!'
            return response

        is_deleted = self.service.delete_recipe(id)
        if is_deleted:
            response.status = 204
            return response
        response.status = 404
        response.data.message = 'recipe not found!'
        return response

    def exec_get_post(self):
        if self.request.method == 'POST':
            return self.post_recipe()
        elif self.request.method == 'GET':
            return self.get_recipes()

    def exec_delete_put(self, id: str):
        if self.request.method == 'PUT':
            return self.put_recipe(id)
        elif self.request.method == 'DELETE':
            return self.delete_recipe(id)