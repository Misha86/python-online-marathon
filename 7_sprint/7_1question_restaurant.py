"""1 question 7 sprint"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract class for different dishes"""

    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    """Class for italian main course 'Fettuccine Alfredo'"""
    name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    """Class for italian dessert 'Tiramisu'"""
    name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    """Class for french main course 'Duck À L'Orange'"""
    name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    """Class for french dessert 'Crème brûlée'"""
    name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")


class Factory(ABC):
    """Abstract class for different factories"""

    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    """Class factory for italian dishes"""

    def get_dish(self, type_of_meal: str) -> Product:
        if type_of_meal == "main":
            return FettuccineAlfredo()
        else:
            return Tiramisu()


class FrenchDishesFactory(Factory):
    """Class factory for french dishes"""

    def get_dish(self, type_of_meal: str) -> Product:
        if type_of_meal == "main":
            return DuckALOrange()
        else:
            return CremeBrulee()


class FactoryProducer:
    """Class produce factory according cuisine type"""

    def get_factory(self, type_of_factory: str):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        else:
            return FrenchDishesFactory()


if __name__ == '__main__':
    fp = FactoryProducer()
    fac = fp.get_factory("italian")
    main_dish = fac.get_dish("main")
    main_dish.cook()



