# Write a program that overload the + operator so that it can add two object of class fraction

class add:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return str(self.x)+" "+str(self.y)
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return add(x,y)

p1=add(2,3)
print(p1)
p2=add(3,4)
print(p2)
p4=p1+p2
print("Addition",p4)

