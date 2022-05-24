class Dessert:
    def __init__(self, name='', calories: int = 0):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        if isinstance(self.__calories, (int, float)) and self.__calories < 200:
            return True
        else:
            try:
                return int(self.__calories) < 200
            except ValueError:
                return False

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


d1 = Dessert('aaa', 199.6)
print(d1.calories)
print(d1.is_healthy())
print(d1.is_delicious())
