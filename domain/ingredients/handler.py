import json
from domain.ingredients.service import ServiceIngredient
from domain.ingredients.models.ingredient import Ingredient
from api.utils.response_generic import ResponseGeneric

class HandleIngredient:
    def __init__(self, request):
        self.request = request        
        self.service = ServiceIngredient()

    def get_ingredients(self):
        items = self.service.get_all_ingredients()
        response = ResponseGeneric()
        response.data.items = items
        return response

    def post_ingredient(self):
        response = ResponseGeneric()
        try:
            ingredient = json.loads(self.request.data, object_hook=lambda d: Ingredient(**d))
            if self.service.create_ingredient(ingredient):
                response.status = 201
                response.message = 'Created!'
            else:
                response.status = 500
                response.message = 'Internal server error!'
        except:
            response.status = 400
            response.message = 'Bad Request'
        return response

    def put_ingredient(self, id: str):
        response = ResponseGeneric()
        try:
            ingredient = json.loads(self.request.data, object_hook=lambda d: Ingredient(**d))
            if self.service.update_ingredients(ingredient, id):
                response.message = 'Success'
                response.status = 200
            else:
                response.message = 'Internal server error!'
                response.status = 500
        except:
            response.status = 400
            response.message = 'Bad Request'
        return response

    def delete_ingredient(self, id: str):
        response = ResponseGeneric()
        if len(id) < 1:
            response.status = 400
            response.data.message = 'Required id value!'
            return response

        is_deleted = self.service.delete_ingredient(id)
        if is_deleted:
            response.status = 204
            return response
        response.status = 404
        response.data.message = 'Ingredient not found!'
        return response

    def exec_get_post(self):
        if self.request.method == 'POST':
            return self.post_ingredient()
        elif self.request.method == 'GET':
            return self.get_ingredients()

    def exec_delete_put(self, id: str):
        if self.request.method == 'PUT':
            return self.put_ingredient(id)
        elif self.request.method == 'DELETE':
            return self.delete_ingredient(id)