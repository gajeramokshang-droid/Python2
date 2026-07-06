class Student:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    def putdata(self):
        print("Name:",self.name,"Email:",self.email)
    
class phDguide:
    def __init__(self,name,email,students):
        self.name=name
        self.email=email
        self.students=students

    def putdata(self):
        print("Name:",self.name,"Email:",self.email,"Student:",self.students)
    
    def add(self,newmember):
       return self.students.append(newmember)
    
    def remove(self,removes):
        if(removes in self.students):
           return self.students.remove(removes)
        else:
            print("Student not found!")


p1=Student("Mokshang","SJLHIG")
p1.putdata()

p2=phDguide("Mokshang","Gajera@gmail.com",["Jesus","Me","Holy Spirit"])
p2.putdata()
p2.add("Mokshau")
p2.putdata()
p2.remove("Mokshau")
p2.putdata()

