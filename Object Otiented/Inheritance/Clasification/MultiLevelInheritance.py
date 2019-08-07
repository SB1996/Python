# MultiLevel Inheritance in Python ...!

class GrandParent:
    def __init__(self):
        print("GrandParent class constructor call...")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent class constructor call...")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor call...")


print("___________________________________________")
objG = GrandParent()
print("___________________________________________")
objP = Parent()
print("___________________________________________")
objC = Child()
print("___________________________________________")
