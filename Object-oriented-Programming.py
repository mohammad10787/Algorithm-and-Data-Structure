# Object Oriented Programming in Python for a Parking lot
# The parking has 20 available parking spaces for 5 dollar an hour
# For over 20 hours the car pays 100
# We will define 2 classes

# Car Class

class Car:
    # Class constructor
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color

    def __repr__(self):
        return f'{self.license_plate}, {self.model}, {self.color}'

class Garage:

    def __init__(self):
        self.cars_added = []
        self.spots = 20
        self.car_info = {}
        self.bill = 0


if __name__ == '__main__':
    Car1 = Car("9KKH908","Volvo", "Black")
    print(Car1.__repr__())
