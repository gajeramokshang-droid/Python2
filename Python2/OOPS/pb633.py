# Implement the following hierarchy . The Staff function has name and salary as its data members, the derived class
# Teaching has subject as its data member and the class NonTeaching has department as its data member. The derived
# class method overrides (extends) the methods of the base class.

class jesus:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
    def display(self):
        print("Salary is:",self.salary,"Name is:",self.name)
    
class Teaching(jesus):
    def __init__(self,subject,name,salary):
        super().__init__(name, salary)
        self.subject=subject
    
    def display(self):
        super().display()
        print("Subject is:",self.subject)

class NonTeaching(jesus):
    def __init__(self, name, salary,department):
        super().__init__(name,salary)
        self.department=department
    
    def display(self):
        super().display()
        print("Department:",self.department)

p1=Teaching("Maths","Mokshang",250000)
p1.display()

p2=NonTeaching("Mokshang",250000,"cse")
p2.display()

