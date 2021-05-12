import json
from types import SimpleNamespace
from domain.cakes.service import Servicecakes
from domain.cakes.models.cake import Cake
from api.utils.response_generic import ResponseGeneric

class HandleCakes:
    def __init__(self, request):
        self.request = request        
        self.service = Servicecakes()

    def get_cakes(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def post_cake(self):
        cake = json.loads(self.request.data, object_hook=lambda d: Cake(**d))
        if type(cake) is not Cake:
            return ResponseGeneric('Bad Request!', 400)
            
        self.service.create_cakes(cake)
        return ResponseGeneric('Still woozy ma friend', 200)

    def patch_cake(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def delete_cake(self):
        return ResponseGeneric('Still woozy ma friend', 200)

    def exec(self):
        if self.request.method == 'POST':
            return self.post_cake()
        elif self.request.method == 'GET':
            return self.get_cakes()
        elif self.request.method == 'PATCH':
            return self.patch_cake()
        elif self.request.method == 'DELETE':
            return self.delete_cake()