class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return str(self.x)+" "+str(self.y)
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x, y)
    
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return point(x,y)
    
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        return(point(x,y))
    
    def __truediv__(self,other):
        x=self.x/other.x
        y=self.y/other.y
        return point(x,y)
    
    def __pow__(self,other):
        x=self.x**other.x
        y=self.y**other.y
        return point(x,y)
    
    def __mod__(self,other):
        x=self.x%other.x
        y=self.y%other.y
        return point(x,y)

    
p1=point(2,3)
print(p1)
p2=point(3,4)
print(p2)

p3=p1+p2
print(p3)

p4=p2-p1
print(p4)

p5=p1*p2
print(p5)

p6=p1/p2
print(p6)

p7=p1 ** p2
print(p7)

p8=p1%p2
print(p8)