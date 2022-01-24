"""2 question 4 sprint"""
from enum import Enum


class TypePizza(Enum):
    """Ingredients for different type of pizza"""
    garden_feast = ["spinach", "olives", "mushroom"]
    meat_festival = ["beef", "meatball", "bacon"]
    hawaiian = ["ham", "pineapple"]


class Pizza:
    """
    Order Pizza
    """
    __count_orders = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

        self.__class__.__count_orders += 1
        self._order_number = self.__count_orders

    @property
    def order_number(self):
        return self._order_number

    @classmethod
    def garden_feast(cls):
        return cls(TypePizza.garden_feast.value)

    @classmethod
    def meat_festival(cls):
        return cls(TypePizza.meat_festival.value)

    @classmethod
    def hawaiian(cls):
        return cls(TypePizza.hawaiian.value)


if __name__ == '__main__':
    p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
    p2 = Pizza.garden_feast()  # order 2
    print(p1.ingredients)
    print(p2.ingredients)
    print(p1.order_number)
    print(p2.order_number)
    print(p2.order_number)

