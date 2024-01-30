class A:
    def __init__(self):
        print("Hello from Class A Constructor")

    def greet_A(self):
        print("Hey From greet_A Method ")

class B(A):
    def __init__(self):
        super().__init__()
        print("Hello  From Class B Constructor")
    def greet_B(self):
        print("Hey From greet_B Method")


obj1=A()        # A class Object is created.
obj1.greet_A()  # It calls Base class Properties.

    # It Calls Base class Properties by using child class object beacuse of inheritance.
obj2=B()  # B class Object is created.
obj2.greet_B()


