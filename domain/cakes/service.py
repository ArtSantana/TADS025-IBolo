from domain.cakes.models.cake import Cake
from typing import Type, TypeVar

class ServiceCakes:
    def create_cake(self, cake: Type[Cake]):
        print(cake.name, cake.unit, cake.price)

    def get_cakes(self):
        print('getting cakes')
    
    def delete_cake(self, id: str):
        print(id)

    def update_cake(self, cake: Type[Cake]):
        print(cake)