# Program to demonstrate the issue of invoking __init__() in case of multiple inheritance

class parent1:
    def __init__(self,x):
        self.x=x
    
    def display(self):
        print("X:",self.x)
    
class parent2:
    def __init__(self,y):
        self.y=y
    
    def display2(self):
        print("Y:",self.y)

class child(parent1,parent2):
    def __init__(Self,x):
        super().__init__(x)

    
    def display3(self):
        print("Child")

c3=child(10)
c3.display()
c3.display3()
c3.display2()

