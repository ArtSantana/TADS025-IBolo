class Cake:
    def __init__(self, price, recipe_id):
        self.__price = price
        self.__recipe_id = recipe_id # like kg, g, l

    def set_recipe_id(self, recipe_id):
        self.__recipe_id = recipe_id

    def set_price(self, price):
        self.__price = price

    def get_recipe_id(self):
        return self.__recipe_id

    def get_price(self):
        return self.__price