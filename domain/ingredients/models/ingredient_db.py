class IngredientDB:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.price = 0
        self.unit = ''

    def parseFromDict(self, igrendient_dict):
        self.id = str(igrendient_dict['_id'])
        self.name = igrendient_dict['_Ingredient__name']
        self.price = igrendient_dict['_Ingredient__price']
        self.unit = igrendient_dict['_Ingredient__unit']