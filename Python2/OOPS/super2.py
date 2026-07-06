class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")
        

class C(A):
    def greet(self):
        super().greet()
        print("Hello from C")
      

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()

print(D.mro())
