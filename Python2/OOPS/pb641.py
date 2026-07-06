# Create a class student with following member attributes: roll no, name, age and total marks. Create suitable methods for
# reading and printing member variables. Write a python program to overload ‘==’ operator to print the details of students
# having same marks

class Student:
    def __init__(self, rollno, name, age, totalmarks):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.totalmarks = totalmarks

    def display(self):
        print("Roll:", self.rollno,
              "Name:", self.name,
              "Age:", self.age,
              "Total Marks:", self.totalmarks)

    def __eq__(self, other):
        if self.totalmarks == other.totalmarks:
            print("\nStudents having same marks:")
            self.display()
            other.display()
            return True
        else:
            print("\nStudents do not have same marks.")
            return False


p1 = Student(18, 'Mokshang', 18, 29)
p2 = Student(19, 'Jesus', 19, 29)
p3=p1 == p2
print(p3)

