class Vehicle:
    def show(self):
        print("Different types of Vehicles:\n")


class Truck(Vehicle):
    def show_info(self):
        print("This is a Truck.")


class Bus(Vehicle):
    def show_info(self):
        print("This is a Bus.")


class Car(Vehicle):
    def show_info(self):
        print("This is a Car.")


class Bike(Vehicle):
    def show_info(self):
        print("This is a Bike.")



v = Vehicle()
v.show()

t = Truck()
t.show_info()

b = Bus()
b.show_info()

c = Car()
c.show_info()

bk = Bike()
bk.show_info()
