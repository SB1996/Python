# Multiple Inheritance in Python ...!

class DriveClass:
   def __init__(self):
        print("DriveClass00 constructor call...")

class AnotherDriveClass:
   def __init__(self):
        print("DriveClass01 constructor call...")

# inherited DriveClass, AnotherDriveClass(Parent class) classes into SubClass(Child class)
class SubClass(DriveClass,AnotherDriveClass):
    def __init__(self):
        super().__init__()
        print("SubClass constructor call...")

