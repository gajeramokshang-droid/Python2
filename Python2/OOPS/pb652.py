# Write a python program to create a Bus child class that inherits from the Vehicle class.
# In Vehicle class vehicle name, mileage and seatingcapacity as its data member. The default fare charge of any vehicle is
# seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So
# total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Sample Output:
# The bus seating capacity is 50. so, the final fare amount should be 5000+500=5500.
# The car seating capacity is 5. so, the final fare amount should be 500.


class Vehicle:
    def __init__(self,name,mileage,seatingcapacity):
        self.name=name
        self.mileage=mileage
        self.seatingcapacity=seatingcapacity
    
    def faircharge(self):
        return self.seatingcapacity*100
    
class Bus(Vehicle):
    def __init__(self, name, mileage, seatingcapacity):
        super().__init__(name, mileage, seatingcapacity)

    def faircharge(self):
        base_fair=super().faircharge()
        maintainance=base_fair*0.10
        return maintainance

bus=Vehicle("Mokshang",10,50)
print("Faircharge=",bus.faircharge())   

p1=Bus("Mokshang",15,5)
print(p1.faircharge())
