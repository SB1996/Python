# Multiple Inheritance in Python ...!
class DriveClass:
   def __init__(self):
        print("DriveClass constructor call...")

   def show(self):
       print("DriveClass show() call...")

class AnotherDriveClass:
   def __init__(self):
        print("AnotherDriveClass constructor call...")

   def show(self):
       print("AnotherDriveClass show() call...")



# inherited DriveClass, AnotherDriveClass(Parent class) classes into SubClass(Child class)
class SubClass(DriveClass,AnotherDriveClass):
    def __init__(self):
        super().__init__()

        DriveClass.__init__(self)
        AnotherDriveClass.__init__(self)

        print("SubClass constructor call...")


subObject = SubClass()
subObject.show()



########################################################################################################################

# Hybrid Inheritance in Python ...!
class Parent:
    def __init__(self):
        print("Parent class constructor call...")

    def show(self):
       print("ParentClass show() call...")


# inherited DriveClass(Parent class) class into SubClass(Child class)
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child00 class constructor call...")

    def show(self):
       print("AnotherDriveClass show() call...")

# inherited DriveClass(Parent class) class into SubClass(AnotherChild class)
class AnotherChild(Parent):
    def __init__(self):
        super().__init__()
        print("Child01 class constructor call...")

    def show(self):
       print("AnotherDriveClass show() call...")


class grandChild(Child,AnotherChild):
    def __init__(self):
        super().__init__()
        print("grandChild class constructor call...")


grangObject = grandChild()
grangObject.show()