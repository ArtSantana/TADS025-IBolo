import json

from werkzeug.local import LocalProxy
from domain.ingredients.service import ServiceIngredient
from domain.ingredients.models.ingredient import Ingredient
from api.utils.response_generic import ResponseGeneric

class HandleIngredient:
    def __init__(self, request):
        self.request: LocalProxy = request        
        self.service = ServiceIngredient()
        self.response = ResponseGeneric()

    def get_ingredients(self):
        items = self.service.get_all_ingredients()
        self.response.data.items = items

    def post_ingredient(self):
        try:
            ingredient = json.loads(self.request.data, object_hook=lambda d: Ingredient(**d))
            if self.service.create_ingredient(ingredient):
                self.response.set_message_and_status('Created!', 201)
            else:
                self.response.set_message_and_status('Internal server error!', 500)
        except:
            self.response.set_message_and_status('Bad Request', 400)

    def put_ingredient(self, id: str):
        try:
            ingredient = json.loads(self.request.data, object_hook=lambda d: Ingredient(**d))
            if self.service.update_ingredients(ingredient, id):
                self.response.set_message_and_status('Success', 200)
            else:
                self.response.set_message_and_status('Internal server error!', 500)
        except:
            self.response.set_message_and_status('Bad Request!', 400)

    def delete_ingredient(self, id: str):
        if len(id) < 1:
            self.response.set_message_and_status('Required id value!', 400)
            return

        is_deleted = self.service.delete_ingredient(id)
        if is_deleted:
            self.response.status = 204
            return
        self.response.set_message_and_status('Ingredient not found!', 404)

    def exec_get_post(self):
        if self.request.method == 'POST':
            self.post_ingredient()
        elif self.request.method == 'GET':
            self.get_ingredients()
        return self.response

    def exec_delete_put(self, id: str):
        if self.request.method == 'PUT':
            self.put_ingredient(id)
        elif self.request.method == 'DELETE':
            self.delete_ingredient(id)
        return self.response