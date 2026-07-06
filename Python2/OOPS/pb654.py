# Write a python program to demonstrate the use of super() method to call the method of base class.

class jesus:
    def jesus1(self):
        print("Mokshang")

class mary(jesus):
    def jesus1(self):
        return super().jesus1()

jes=mary()
jes.jesus1()

