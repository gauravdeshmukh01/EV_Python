# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def moves(self):
#         print("move along...")

#     def get_make_model(self):
#         print(f"This car is manifactured by {self.make} and the model is {self.model}.")
    
# # my_car = Vehicle("Toyota", "Corolla")
# # my_car.moves()
# # my_car.get_make_model()
# # print(my_car.make)
# # print(my_car.model)
# # print(type(my_car))

# your_car = Vehicle("Honda", "Civic")
# your_car.moves()
# your_car.get_make_model()
# print(your_car.make)
# print(your_car.model)

# *****************************************************************************

# # Inheritance Example

# class Airplane(Vehicle):
#     def moves(self):
#         print("fly high in the sky...")

# class Truck(Vehicle):
#     def moves(self):
#         print("drive on the road...")

# class GolfCart(Vehicle):
#     pass

# cessna = Airplane("Cessna", "172")
# mack = Truck("Mack", "Anthem")
# golfwagon = GolfCart("Club Car", "Onward")

# cessna.get_make_model()
# cessna.moves()

# mack.get_make_model()
# mack.moves()

# golfwagon.get_make_model()
# golfwagon.moves()

# *****************************************************************************

# Inhereitance example 2

'''
Create a class called Animal() with a method sound() that prints
"Animal makes a sound". Create a derived class called Dog that
inherits from Animal and overrides the sound() method to print "Dog barks".
Create another Derived class called Bird that inherits from
Animal and overrides the sound() method to print "Birds Sing"
'''

# class Animal():
#     def sound(self):
#         print("Animal makes a sound")

# a1=Animal()
# a1.sound()


# class cat(Animal):
#     pass


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d1=Dog()
# d1.sound()


# c1=cat()
# c1.sound()


# class Bird(Animal):
#     def sound(self):
#         print("Birds Sing")

# b1=Bird()
# b1.sound()

# *****************************************************************************

# Create a base class called Shape with a method area() that returns 0.
# Create derived class called Rectangle that inherits from Shape
# and overrides the area() method to calculate and return the area of a rectangle.


# class Shape():
#     def area(self):
#         return 0

# S1 = Shape()
# S1.area()
# print(S1.area())

# method 1
# class Rectangle(Shape):
#     def area (self):
#         l = 10
#         b = 20
#         print("Area of Rectangle is:", l*b)

# r1 = Rectangle()
# r1.area()


# method 2
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# r1 = Rectangle(10, 5)
# print(r1.area())

# *****************************************************************************

# Create a base class called Person with a constructor that takes a name as a parameter.
# Create a derived class called Student that inherits from Person and has a constructor
# that takes a parameter called grade. Write a method in student to display the name
# and grade of the student. Use super keyword to achieve this.

# class Person():
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade = grade

#     def display(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")


# s1 = Student("Gaurav", "A")
# s1.display()

# *****************************************************************************

# Create a base class called Employee with properties name and salary.
# Create a derived class called Manager that inherits from Employee
# and adds property department. Write a method in Manager to display
# the name, salary and department of the manager.

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


m1 = Manager("Gaurav", 56000, "IT")
m1.display()
        