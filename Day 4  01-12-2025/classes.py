class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("move along...")

    def get_make_model(self):
        print(f"This car is manifactured by {self.make} and the model is {self.model}.")
    
# my_car = Vehicle("Toyota", "Corolla")
# my_car.moves()
# my_car.get_make_model()
# print(my_car.make)
# print(my_car.model)
# print(type(my_car))

your_car = Vehicle("Honda", "Civic")
your_car.moves()
your_car.get_make_model()
print(your_car.make)
print(your_car.model)

# *****************************************************************************

# Inheritance Example

class Airplane(Vehicle):
    def moves(self):
        print("fly high in the sky...")

class Truck(Vehicle):
    def moves(self):
        print("drive on the road...")

class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna", "172")
mack = Truck("Mack", "Anthem")
golfwagon = GolfCart("Club Car", "Onward")

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

# *****************************************************************************