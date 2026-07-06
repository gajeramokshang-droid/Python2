
class Father:
    def father(self):
        print("Jesus")

class Mother:
    def mother(self):
        print("Holy Spirit")

class Children(Father,Mother):
    def child(self):
        print("Mokshang")

p1=Children()
p1.father()
p1.mother()
p1.child()
print(Mother.mro())
print(Children.mro())
