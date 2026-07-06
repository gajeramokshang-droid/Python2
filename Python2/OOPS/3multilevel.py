class gp:
    def grandpa(self):
        print("Father")

class parent(gp):
    def paren(self):
        print("Son")

class children(parent):
    def child(self):
        print("HolySpirit")

p1=children()
p1.grandpa()
p1.paren()
p1.child()
print(children.mro())
