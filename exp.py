class Vehicle:
    def type(self):
        return "This is a vehicle."

class Bike(Vehicle):
    def type(self):
        return "This is a bike."

b = Bike()
print(b.type())