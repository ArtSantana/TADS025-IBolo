import json
from typing import Type

from werkzeug.local import LocalProxy
from domain.cakes.service import ServiceCake
from domain.cakes.models.cake import Cake
from api.utils.response_generic import ResponseGeneric

class HandleCake:
    def __init__(self, request):
        self.request: LocalProxy = request        
        self.service = ServiceCake()
        self.response = ResponseGeneric()

    def get_cakes(self) -> None:
        items = self.service.get_all_cakes()
        self.response.data.items = items

    def post_cake(self) -> None:
        try:
            cake = json.loads(self.request.data, object_hook=lambda d: Cake(**d))
            if self.service.create_cake(cake):
                self.response.set_message_and_status('Created!', 201)
            else:
                self.response.set_message_and_status('Internal server error!', 500)
        except:
            self.response.set_message_and_status('Bad request!', 400)

    def put_cake(self, id: str) -> None:
        try:
            cake = json.loads(self.request.data, object_hook=lambda d: Cake(**d))
            if self.service.update_cakes(cake, id):
                self.response.set_message_and_status('Success!', 200)
            else:
                self.response.set_message_and_status('Internal server error!', 500)
        except:
            self.response.set_message_and_status('Bad Request', 400)

    def delete_cake(self, id: str) -> None:
        if len(id) < 1:
            self.response.set_message_and_status('Required id value!', 400)
            return

        is_deleted = self.service.delete_cake(id)
        if is_deleted:
            self.response.status = 204
            return
        self.response.set_message_and_status('cake not found', 404)

    def exec_get_post(self) -> Type[ResponseGeneric]:
        if self.request.method == 'POST':
            self.post_cake()
        elif self.request.method == 'GET':
            self.get_cakes()
        return self.response

    def exec_delete_put(self, id: str) -> Type[ResponseGeneric]:
        if self.request.method == 'PUT':
            self.put_cake(id)
        elif self.request.method == 'DELETE':
            self.delete_cake(id)
        return self.response