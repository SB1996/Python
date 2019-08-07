# Hybrid Inheritance in Python ...!

class Parent:
    def __init__(self):
        print("Parent class constructor call...")


# inherited DriveClass(Parent class) class into SubClass(Child class)
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child00 class constructor call...")

# inherited DriveClass(Parent class) class into SubClass(AnotherChild class)
class AnotherChild(Parent):
    def __init__(self):
        super().__init__()
        print("Child01 class constructor call...")


class grandChild(Child,AnotherChild):
    def __init__(self):
        super().__init__()
        print("grandChild class constructor call...")
