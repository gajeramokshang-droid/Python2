class parent:
    def father(self):
        print("Jesus")

class children(parent):
    def child(self):
        print("Mokshang")

p1=children()
p1.father()
p1.child()
print(children.mro())

