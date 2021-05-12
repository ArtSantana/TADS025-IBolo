class Ingredient:
    def __init__(self, name, price, unit):
        self.__name = name
        self.__price = price
        self.__unit = unit # like kg, g, l

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setUnit(self, unit):
        self.__unit = unit

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getUnit(self):
        return self.__unit