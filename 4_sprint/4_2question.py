"""2 question 4 sprint"""


class Pizza:
    """
    Order Pizza
    """
    __order_number = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self._order_number = self.__set_order_number()

    @property
    def order_number(self):
        return self._order_number

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def __set_order_number(cls):
        cls.__order_number += 1
        return cls.__order_number


if __name__ == '__main__':
    p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
    p2 = Pizza.garden_feast()  # order 2
    print(p1.ingredients)
    print(p2.ingredients)
    print(p1.order_number)
    print(p2.order_number)

