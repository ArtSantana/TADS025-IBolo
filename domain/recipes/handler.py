import json
from typing import Type
from types import SimpleNamespace

from werkzeug.local import LocalProxy
from domain.recipes.service import ServiceRecipe
from domain.recipes.models.recipe import Recipe
from api.utils.response_generic import ResponseGeneric

class HandleRecipe:
    def __init__(self, request):
        self.request: LocalProxy = request        
        self.service = ServiceRecipe()
        self.response = ResponseGeneric()

    def get_recipes(self) -> None:
        items = self.service.get_all_recipes()
        self.response.data.items = items

    def post_recipe(self) -> None:
        recipe_request = json.loads(self.request.data, object_hook=lambda d: SimpleNamespace(**d))
        recipe = Recipe()
        try:
            recipe.parseFromRequest(recipe_request)
        except:
            self.response.set_message_and_status('Bad request!', 400)
        if self.service.create_recipe(recipe):
            self.response.set_message_and_status('Created!', 201)
        else:
            self.response.set_message_and_status('Internal server error!', 500)

    def put_recipe(self, id: str) -> None:
        recipe_request = json.loads(self.request.data, object_hook=lambda d: SimpleNamespace(**d))
        recipe = Recipe()
        recipe.parseFromRequest(recipe_request)
        if self.service.update_recipes(recipe, id):
            self.response.set_message_and_status('Success!', 200)
        else:
            self.response.set_message_and_status('Internal server error!', 500)

    def delete_recipe(self, id: str) -> None:
        if len(id) < 1:
            self.response.set_message_and_status('Required id value!', 400)
            return

        is_deleted = self.service.delete_recipe(id)
        if is_deleted:
            self.response.status = 204
            return
        self.response.status = 404
        self.response.data.message = 'recipe not found!'

    def exec_get_post(self) -> Type[ResponseGeneric]:
        if self.request.method == 'POST':
            self.post_recipe()
        elif self.request.method == 'GET':
            self.get_recipes()
        return self.response

    def exec_delete_put(self, id: str) -> Type[ResponseGeneric]:
        if self.request.method == 'PUT':
            self.put_recipe(id)
        elif self.request.method == 'DELETE':
            self.delete_recipe(id)
        return self.response