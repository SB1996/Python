# Inheritance in Python ...!

class DriveClass:
    # Class variable...
    publicData = "public ststic Data" # public data attribute.
    _protectedData = "protected ststic Data" # protected data attribute.
    __privateData = "private ststic Data" # private data attribute.

    def __init__(self):
        print("DriveClass constructor call...")


# inherited DriveClass(Parent class) class into SubClass(Child class)
class SubClass(DriveClass):

    def __init__(self):
        super().__init__()
        print("SubClass constructor call...")




objDrive = DriveClass()
objSub = SubClass()
