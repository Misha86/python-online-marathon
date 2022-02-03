"""2 question 7 sprint"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

    def price_after_discount(self):
        if not self.discount_strategy:
            return self.price
        return self.discount_strategy(self)


def on_sale_discount(order: Goods):
    return order.price/2


def twenty_percent_discount(order: Goods):
    return order.price*0.8


if __name__ == '__main__':
    good = Goods(100)
    print(good)
    print(good.price)
    print(good.price_after_discount())
    good.discount_strategy = on_sale_discount
    print(good.price_after_discount())
    good.discount_strategy = twenty_percent_discount
    print(good.price_after_discount())
    print(on_sale_discount(good))






