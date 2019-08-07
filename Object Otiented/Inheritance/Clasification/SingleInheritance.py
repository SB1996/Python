# Single Inheritance in Python ...!

class DriveClass:

   def __init__(self):
        print("DriveClass constructor call...")


# inherited DriveClass(Parent class) class into SubClass(Child class)
class SubClass(DriveClass):

    def __init__(self):
        super().__init__()
        print("SubClass constructor call...")