class parent:
    def paren(self):
        print("Jesus")

class children(parent):
    def child1(self):
        print("Mokshang")

class children2(parent):
    def child2(self):
        print("Riteshbhai")

class children3(parent):
    def child3(self):
        print("Gajera")

p1=children()
p1.paren()
p1.child1()

p2=children2()
p2.paren()
p2.child2()

p3=children3()
p3.paren()
p3.child3()

print(children3.mro())
