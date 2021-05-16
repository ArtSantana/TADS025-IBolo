class CakeDB:
    def __init__(self):
        self.id = ''
        self.recipe_id = ''
        self.price = 0

    def parseFromDict(self, cake_dict):
        self.id = str(cake_dict['_id'])
        self.recipe_id = cake_dict['_Cake__recipe_id']
        self.price = cake_dict['_Cake__price']