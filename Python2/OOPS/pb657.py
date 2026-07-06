# Create three Class Employee, Perks, NetSalary. Make an Employee class as an abstract class.
# Employee class should have methods for following tasks.
# - To get employee details like employee id, name and salary from user.
# - To print the Employee details.
# - return Salary.
# - An abstract method emp_id.
# Perks class should have methods for following tasks.
# - To calculate DA, HRA, PF.
# - To print the individual and total of Perks (DA+HRA-PF).
# Netsalary class should have methods for following tasks.
# - Calculate the total Salary after Perks.
# - Print employee detail also prints DA, HRA, PF and net salary.
# Note 1: DA-35%, HRA-17%, PF-12%
# Note 2: It is compulsory to create objects and demonstrating the methods with
# Correct output. Example:
# Employee ID: 1
# Employee Name: John
# Employee Basic Salary: 25000
# DA: 8750.0
# HRA: 4250.0
# PF: 3000.0
# Total Salary: 35000.0


from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
    
    def get_emp(self):
        self.employee_id=int(input("Enter an employee id:"))
        self.name=input("Enter an employee name:")
        self.salary=int(input("Enter a salary:"))
    
    def display(self):
        print("EMPID=",self.employee_id,"NAME=",self.name,"SALARY=",self.salary)
    
    def get_salary(self):
        return self.salary
    
    @abstractmethod
    def emp_id(self):
        pass

class Perk(Employee):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name, salary)
        self.da=0
        self.hra=0
        self.pf=0
    
    def calculate(self):
        self.da=self.salary*0.35
        self.hra=self.salary*0.17
        self.pf=self.salary*0.12
    
    def display_perk(self):
        
        print("DA=",self.da)
        print("HRA=",self.hra)
        print("PF=",self.pf)
       
    
    def emp_id(self):
        return self.employee_id

class NetSalary(Perk):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name, salary)
        self.net_salary = 0

    def calculate_net_salary(self):
        self.net_salary = self.salary + (self.da + self.hra - self.pf)

    def display_net_salary(self):
        print("NET SALARY =", self.net_salary)

p=NetSalary(0,"",0)
p.get_emp()
p.display()

p.calculate()
p.display_perk()

p.calculate_net_salary()
p.display_net_salary()
