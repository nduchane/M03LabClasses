# Nicholas DuChane
# M03LabClasses
# Creates a Vehicles and automotive class and gets users info for those.
# Variables include Automotive with parameters.

# Classes
class Vehicle:
    def __init__(self, name):
        self.name = name
class Automobile(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Program start
print("What type of vehicle is this?")
userveh = Automobile(input())
print("year?")
userveh.year = input()
print("make?")
userveh.make = input()
print("model?")
userveh.model = input()
print("doors?")
userveh.doors = input()
print("roof?")
userveh.roof = input()

# Program end | Print user inputs
print("Vehicle type: " + userveh.name)
print("Year: " + userveh.year)
print("Make: " + userveh.make)
print("Model: " + userveh.model)
print("Number of doors: " + userveh.doors)
print("Type of roof: " + userveh.roof)
