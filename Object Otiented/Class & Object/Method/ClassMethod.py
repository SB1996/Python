# class method in python ...!

# class Method :  1. A class method is a method which is bound to the class and not the object of the class.
#
#                 2. They have the access to the state of the class as it takes a class parameter that points
#                    to the class and not the object instance.
#
#                 3. It can modify a class state that would apply across all the instances of the class.
#                    For example it can modify a class variable that will be applicable to all the instances.

class Details:
    # Class Attributes(Class Variable)...
    name = "Santanu Banik"
    age = 23

    # Constructor...
    def __init__(self):
        # Instance Attributes(Instance Variable)...
        self.name = "Banti"


    @classmethod
    def show(cls):
        print(f"Name : {Details.name}")
        print(f"Age : {cls.age}")

