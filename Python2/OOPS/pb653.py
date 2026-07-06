# Create an abstract class named Shape.
# Create an abstract method named calculate_area for the Shape class.
# Create Two Classes named Rectangle and Circle which inherit Shape class.
# Create calculate_area method in Rectangle class. It should return the area of the rectangle object. (area of rectangle =
# (length * breadth))
# Create calculate_area method in Circle class. It should return the area of the circle object.
# (area of circle =πr^2))
# Create objects of Rectangle and Circle class.
# The python Program Should also check whether the area of one Rectangle object is greater
# than another rectangle object by overloading > operator.
# Execute the method resolution order of the Circle class.

from abc import ABC,abstractmethod
import math
class shape:
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def calculate_area(self):
        print(self.length*self.breadth)
class circle(shape):
    def __init__(self,r):
        self.r=r

    def calculate_area(self):
        return math.pi*self.r*self.r
    
Reactangl=Rectangle(12,13)
p1=Reactangl.calculate_area()

Circle=circle(12)
c1=Circle.calculate_area()
print("Area of circle:",c1)

