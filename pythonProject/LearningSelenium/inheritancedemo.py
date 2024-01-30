class A:
    def __init__(self):
        print("Hello from Class A Constructor")

    def greet_A(self):
        print("Hey From greet_A Method ")

class B(A):
    pass

obj1=A()        # A class Object is created.
obj1.greet_A()  # It calls Base class Properties.

    # It Calls Base class Properties by using child class object beacuse of inheritance.
obj2=B()  # B class Object is created.
obj2.greet_A()


