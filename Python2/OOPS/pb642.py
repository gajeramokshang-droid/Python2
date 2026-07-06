# Write a program to create a class called Data having “value” as its data member. Overload the (>) and the (<) operator for
# the class. Instantiate the class and compare the objects using _lt_ and _gt_.

class Data:
    def __init__(self,value):
        self.value=value
    
    def __str__(self):
        return str(self.value)
    
    def __gt__(self,other):
        x=self.value>other.value
        return Data(x)
    
    def __lt__(self,other):
        x=self.value<other.value
        return Data(x)

p1=Data(12)
print(p1)
p2=Data(32)
print(p2)
p3=p1>p2
print(p3)
p4=p1<p2
print(p4)

