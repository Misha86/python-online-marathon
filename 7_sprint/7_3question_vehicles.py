"""3 question 7 sprint"""
from __future__ import annotations


class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    """Class for Car"""

    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(**adapted_methods, **self.obj.__dict__)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        if attr not in self.__dict__:
            pass

    def original_dict(self):
        """Print original object dict"""
        print(self.__dict__['obj'])


if __name__ == '__main__':
    objects = []
    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels=motorCycle.TwoWheeler))
    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.EightWheeler))
    car = Car()
    objects.append(Adapter(car, wheels=car.FourWheeler))
    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))



