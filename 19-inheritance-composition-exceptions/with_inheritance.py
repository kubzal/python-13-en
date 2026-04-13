# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"Vehicle {self.brand} {self.model} has been started.")

    def stop(self):
        print(f"Vehicle {self.brand} {self.model} has been stopped.")

# Derived classes
class Car(Vehicle):
    pass

# Creating objects
car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Yamaha", "MT-07")
bicycle = Bicycle("Kross", "Level")

# Calling methods
car.start()
motorcycle.start()
bicycle.start()

car.stop()
motorcycle.stop()
bicycle.stop()