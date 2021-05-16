class RecipeDB:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.ingredients = []

    def parseFromDict(self, recipe_dict):
        self.id = str(recipe_dict['_id'])
        self.name = recipe_dict['_Recipe__name']
        self.ingredients = recipe_dict['_Recipe__ingredients']