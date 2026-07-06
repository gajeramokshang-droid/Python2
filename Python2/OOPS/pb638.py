
class mul:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return str(self.x)+" "+str(self.y)
    
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return mul(x,y)
    
p1=mul(2,3)
print(p1)
p2=mul(2,3)
print(p2)
p3=p1*p2
print(p3)

