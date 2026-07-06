# Create a class Book with attributes title and price.
# Overload the == operator to compare two books by price.

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    
    def __str__(self):
        return str(self.title)+" "+str(self.price)
    
    def __eq__(self,other):
        x=self.price==other.price
        return x
    
p1=Book("Bible",100000000000000000000)
print(p1)
p2=Book("Think like a billioner",234)
print(p2)

p3=p1==p2
print(p3)

