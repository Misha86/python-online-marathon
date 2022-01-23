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

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    def __set_order_number(self):
        self.__class__.__order_number += 1
        return self.__class__.__order_number


if __name__ == '__main__':
    p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
    p2 = Pizza.garden_feast()  # order 2
    print(p1.ingredients)
    print(p2.ingredients)
    print(p1.order_number)
    print(p2.order_number)

