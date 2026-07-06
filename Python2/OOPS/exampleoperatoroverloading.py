class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return str(self.name)+" "+str(self.marks)
    
    def __gt__(self,other):
        x=self.marks>other.marks
        return x
    
p1=Student("Mokshang",25)
p2=Student("Jesus",100)
print(p1)
print(p2)
print(p2>p1)
