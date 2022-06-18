from abc import ABC, abstractmethod

class Engine:
    """ Abstract class engine """

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def wheel(self):
        return self.vehicle.wheel_number(Vehicle)


class ElectricEngine(Engine):
    """ Subclass Electric engine. """

    def return_fuel(self):
        print("Electricity")

class CombustionEngine(Engine):
    """ Subclass combustion engine. """

    def return_fuel(self):
        print("Fuel")

class HybridEngine(Engine):
    """ Subclass hybrid engine. """

    def return_fuel(self):
        print("Fuel or Electricity")

class Vehicle(ABC):
    """ Class vehicle """

    @abstractmethod
    def wheel_number(self):
        pass

class Car(Vehicle):
    """ Subclass car """

    def wheel_number(self):
        print("4")

class Bus(Vehicle):
    """ Subclass bus """

    def wheel_number(self):
        print("6")

class Truck(Vehicle):
    """ Subclass truck """

    def wheel_number(self):
        print("10")

if __name__ == "__main__":

    hb20 = ElectricEngine(Car)
    hb20.return_fuel()
    hb20.wheel()

    Tesla = HybridEngine(Bus)
    Tesla.return_fuel()
    Tesla.wheel()

    Volvo = CombustionEngine(Truck)
    Volvo.return_fuel()
    Volvo.wheel()
    