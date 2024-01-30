class A:
    def __init__(self):
        print("Hello Constructor A")
    def displayA(self):
        print("Hello Display A")
class B:
    def __init__(self):
        print("Hello Constructor B")
    def displayB(self):
        print("Hello Display B")
class C(A,B):       #Multiple Inheritance
    def __init__(self):
        super().__init__()      #It calls C(A,B) priority wise who will be first decide on it
        print("Hello From Constructor C")
    def displayC(self):
        print("Hello display C")
c=C()
c.displayA()
c.displayB()
c.displayC()

b=B()
b.displayB()

a=A()
a.displayA()
