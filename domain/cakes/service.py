from domain.cakes.models.cake import Cake
from domain.cakes.models.cake_db import CakeDB
from domain.cakes.repository import RepositoryCake
from typing import Type

class ServiceCake:
    def __init__(self):
        self.repository = RepositoryCake()

    def create_cake(self, cake: Type[Cake]):
        return self.repository.insert(cake)
    
    def get_all_cakes(self) -> list:
        list = self.repository.get_all()
        obj_list = []
        for document in list:
            parsed_cake = CakeDB()
            parsed_cake.parseFromDict(document)
            obj_list.append(parsed_cake.__dict__)
        return obj_list

    
    def delete_cake(self, id: str):
        return self.repository.delete(id)

    def update_cakes(self, cake: Type[Cake], id: str):
        return self.repository.update_cake(cake, id)