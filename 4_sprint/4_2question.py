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
    __number = 1

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self.order_number = self.__number

        self.__class__.__number += 1

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

