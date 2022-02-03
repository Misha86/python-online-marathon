"""1 question 7 sprint"""
from __future__ import annotations


# class Washing:
#     @classmethod
#     def wash(cls):
#         return "Washing..."
#
#
# class Rinsing:
#     @classmethod
#     def rinse(cls):
#         return "Rinsing..."
#
#
# class Spinning:
#     @classmethod
#     def spin(cls):
#         return "Spinning..."
#
#
# class WashingMachine:
#
#     def __init__(self):
#         self.startWashing()
#
#     def startWashing(self):
#         print(Washing.wash(), Rinsing.rinse(), Spinning.spin(), sep='\n')


class Washing:

    def wash(self):
        return "Washing..."


class Rinsing:

    def rinse(self):
        return "Rinsing..."


class Spinning:

    def spin(self):
        return "Spinning..."


class WashingMachine:

    def __init__(self):
        self.wash = Washing()
        self.rinse = Rinsing()
        self.spin = Spinning()
        self.startWashing()

    def startWashing(self):
        print("\n".join([self.wash.wash(), self.rinse.rinse(), self.spin.spin()]))


if __name__ == '__main__':
    d = WashingMachine()
    d.startWashing()
