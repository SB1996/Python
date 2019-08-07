# Method in python ...!

# In python method : 1. Instance Method
#                    2. Class Method
#                    3. Static Method


class Details:
    # Class Attributes(Class Variable)...
    name = "Santanu Banik"
    age = 23

    # Constructor...
    def __init__(self):
        # Instance Attributes(Instance Variable)...
        self.name = "Banti"

    # Methods...(Instance Method)
    def showName(self):
        print(f"name : {self.name}")

    # Static Method ...
    # ________________________________________________________________
    # Using static member of class use :
    #    'Class Name not instance(object)' or 'cls' special reference

    # class method ...
    @classmethod
    def show(cls):
        print(f"Name : {Details.name}")
        print(f"Age : {cls.age}")

    # static method ...
    @staticmethod
    def display():
        print(f"Name : {Details.name}")
        print(f"Age : {Details.age}")