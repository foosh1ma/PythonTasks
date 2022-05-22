class Dessert:
    def __init__(self, name, calories):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        return True if self.__calories < 200 else False

    def is_delicious(self):
        return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories


class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        return True if self.__flavor != 'black licorice' else False


jelly = JellyBean('jelly', 150, 'black licorice')
print(jelly.is_delicious())
print(jelly.is_healthy())
