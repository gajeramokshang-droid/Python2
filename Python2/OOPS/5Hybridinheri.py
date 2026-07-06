
class Animal:
    def ani(self):
        print("Animal")

class Bird(Animal):
    def bird(self):
        print("Bird")

class Mamal(Animal):
    def mamal(self):
        print("mamal")

class Mokshang(Bird,Mamal):
    def moksh(self):
        print("Mokshu")

p1=Mokshang()
p1.ani()
p1.bird()
p1.mamal()
p1.moksh()
print(Mokshang.mro())

