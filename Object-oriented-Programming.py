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

    # Function to return the number of spots available
    def spots_available(self):
        return self.spots

    # This function takes the car info and add the car info to the parking lot
    def add_car(self, car):
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1',
                           'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1',
                           'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
        if self.spots >0:
            self.cars_added.append(str(car).split(','))

            self.spots -= 1

            self.car_info ={'Code': [], "License plate": [],
                            'Model': [], 'Color': []}

            for index, i in enumerate(self.cars_added):
                self.car_info['Code'].append(self.identifier[index])
                self.car_info['License plate'].append(i[0])
                self.car_info['Model'].append(i[1])
                self.car_info['Color'].append(i[2])
            return "car successfully added to the parking lot", self.car_info

        else:
            print(f"We have {self.spots} spots available. I am sorry")

    def remove_car(self, given_code, bill_hours):
        past_len = len(self.car_info['Code'])

        if given_code not in self.car_info['Code']:
            print("We could not find your car. Are you sure you parked your car here?")

        else:
            for index, value in enumerate(self.car_info['Code']):
                if value == given_code:
                    print("Your car's license plate is:",
                          self.car_info['License plate'][index])
                    print("Your car's model is:",
                          self.car_info['Model'][index])
                    print("Your car's color is :",
                          self.car_info['Color'][index])
                    removed_car_index = self.car_info['Code'].pop(index)
                    self.car_info['License plate'].pop(index)
                    self.car_info['Model'].pop(index)
                    self.car_info['Color'].pop(index)

                    self.spots += 1

        if len(self.car_info['Code']) < past_len:
            while True:
                if bill_hours.isnumeric():
                    list_of_time_and_code = [bill_hours, removed_car_index]
                    break
                else:
                    print("Your input must be an integer. Sample input: 5")

                bill_hours = input("Enter for how long you were on the parking lot in hours or 'q' "
                                       "to quit.Example input: 5 -->  ")

                if bill_hours in ['q', 'Q']:
                    break
            if int(list_of_time_and_code[0]) < 20:
                self.bill = int(list_of_time_and_code[0]) * 5
                print(f'Your total bill is ${self.bill}')

            else:
                self.bill = int(list_of_time_and_code[0]) * 5 + 100
                print(f'Your total bill is ${self.bill}')
        # displays all cars in garage


    def cars_in_garage(self):
        for i in self.car_info.items():
            print(i)


if __name__ == '__main__':
    my_garage = Garage()
    print(my_garage.spots_available())
    my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
    my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
    my_garage.add_car(Car('LVG34', 'Optra', 'Red'))
    my_garage.cars_in_garage()
    print(my_garage.remove_car('A1', '10'))
    print(my_garage.spots_available())
