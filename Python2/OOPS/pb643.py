# The following illustration creates a class called data. If no argument is passed while instantiating the class a false is
# returned, otherwise a true is returned.

class data:
    def __init__(self,x=None):
        self.x=x
    
    def check(self):
        if(self.x is None):
            return False
        else:
            return True

p1=int(input("Enter a data:"))
if(p1==""):
    obj=data()

else:
    obj=data(p1)

print(obj.check())

