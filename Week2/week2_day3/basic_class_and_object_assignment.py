# **Basic Class and Object**: Write a Python class and create an object of that class.

class Car:

    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles")

    # Given the distance traveled, update the mileage
    def drive(self, distance_traveled):
        self.mileage = self.mileage + distance_traveled
    

# Create object of the class
car_1 = Car("Toyota", "RAV4", 2023, 3)
car_1.display_info()

# drive method
car_1.drive(20)
car_1.display_info()