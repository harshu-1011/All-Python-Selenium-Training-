class A:
    def __init__(self):
        print("Hello Constructor A")
    def displayA(self):
        print("Hello Display A")
class B(A):     #Multilevel Inheritance
    def __init__(self):
        super().__init__()         #It calls its base class constructor
        print("Hello Constructor B")
    def displayB(self):
        print("Hello Display B")
class C(B):       #Multilevel  Inheritance
    def __init__(self):
        super().__init__()      #It calls its base class constructor
        print("Hello From Constructor C")
    def displayC(self):
        print("Hello display C")
c=C()
c.displayA()
c.displayB()
c.displayC()

b=B()
b.displayB()
b.displayA()

a=A()
a.displayA()