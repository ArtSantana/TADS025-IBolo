import json
from domain.cakes.service import ServiceCake
from domain.cakes.models.cake import Cake
from api.utils.response_generic import ResponseGeneric

class HandleCake:
    def __init__(self, request):
        self.request = request        
        self.service = ServiceCake()

    def get_cakes(self):
        items = self.service.get_all_cakes()
        response = ResponseGeneric()
        response.data.items = items
        return response

    def post_cake(self):
        response = ResponseGeneric()
        try:
            cake = json.loads(self.request.data, object_hook=lambda d: Cake(**d))
            if self.service.create_cake(cake):
                response.status = 201
                response.message = 'Created!'
            else:
                response.status = 500
                response.message = 'Internal server error!'
        except:
            response.status = 400
            response.message = 'Bad Request'
        return response

    def put_cake(self, id: str):
        response = ResponseGeneric()
        try:
            cake = json.loads(self.request.data, object_hook=lambda d: Cake(**d))
            if self.service.update_cakes(cake, id):
                response.message = 'Success'
                response.status = 200
            else:
                response.message = 'Internal server error!'
                response.status = 500
        except:
            response.status = 400
            response.message = 'Bad Request'
        return response

    def delete_cake(self, id: str):
        response = ResponseGeneric()
        if len(id) < 1:
            response.status = 400
            response.data.message = 'Required id value!'
            return response

        is_deleted = self.service.delete_cake(id)
        if is_deleted:
            response.status = 204
            return response
        response.status = 404
        response.data.message = 'cake not found!'
        return response

    def exec_get_post(self):
        if self.request.method == 'POST':
            return self.post_cake()
        elif self.request.method == 'GET':
            return self.get_cakes()

    def exec_delete_put(self, id: str):
        if self.request.method == 'PUT':
            return self.put_cake(id)
        elif self.request.method == 'DELETE':
            return self.delete_cake(id)