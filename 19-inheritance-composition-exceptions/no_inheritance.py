class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"Car {self.brand} {self.model} has been started.")

    def stop(self):
        print(f"Car {self.brand} {self.model} has been stopped.")


class Motorcycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"Motorcycle {self.brand} {self.model} has been started.")

    def stop(self):
        print(f"Motorcycle {self.brand} {self.model} has been stopped.")


class Bicycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"Bicycle {self.brand} {self.model} has been started.")

    def stop(self):
        print(f"Bicycle {self.brand} {self.model} has been stopped.")

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

