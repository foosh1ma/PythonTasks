class Dessert:
    def __init__(self, name='', calories=0):
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
        if not isinstance(calories, (int, float)):
            raise Exception("Wrong input")
        self.__calories = calories


d1 = Dessert()
print(d1.calories)
d1.calories = 10
print(d1.calories)
print(d1.is_healthy())
print(d1.is_delicious())
