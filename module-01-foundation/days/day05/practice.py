from abc import ABC, abstractmethod


# 1. Vehicle hierarchy
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

    # 5. Abstract method
    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


# 2 and 3. Truck uses super() and overrides describe()
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        print(f"{self.make} {self.model}, capacity: {self.capacity} tons")

    def wheels(self):
        return 6


# 4. Polymorphism
vehicles = [
    Car("Toyota", "Corolla"),
    Truck("Volvo", "FH16", 20)
]

for vehicle in vehicles:
    vehicle.describe()
    print(f"Wheels: {vehicle.wheels()}")
    print()
