# ABSTRACTION:which used to provide necessary details of an object and hiding
# the implementation from the users
from abc import ABC,abstractmethod

# Abstract class:
# -class extend with ABC class
# - which should consist of atleast one abstract method
# -it is not possible to create object to abstract class
# Abstract method: a method which doesn't have implementation or body
# -it should contain @abstract_method
# concreate class:
# first of all we should inherit the abstract class
# implementation for the abstract method
# we can create the object
class Bank(ABC):
    def __init__(self,name,accno,balance):
        self.name = name
        self.accno = accno
        self.balance = balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

class SBI(Bank):
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

c1 = SBI('steve',45678987654,8990)


print(f'Intial balance:{c1.balance}')  #8990
c1.deposit(1000)
print(f'Balance after deposit:{c1.balance}') #9990
c1.withdraw(500)
print(f'Balance after Withdrawal:{c1.balance}') #9490




from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    # Abstract method, needs to be overridden by the subclass
    @abstractmethod
    def area(self):
        pass

    # Concrete method (not abstract)
    def describe(self):
        print("This is a shape.")

# Subclass 1: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the abstract method
    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass 2: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Overriding the abstract method
    def area(self):
        return self.width * self.height

# Create objects of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the methods
circle.describe()  # Inherited from Shape class
print(f"Area of the circle: {circle.area()}")  # Area method from Circle class

rectangle.describe()  # Inherited from Shape class
print(f"Area of the rectangle: {rectangle.area()}")  # Area method from Rectangle class


