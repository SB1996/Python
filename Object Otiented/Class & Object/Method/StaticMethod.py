# static method in python ...!

# static method : 1. A static method is also a method which is bound to the class and not the object of the class.
#                 2. A static method can’t access or modify class state.
#                 3. It is present in a class because it makes sense for the method to be present in class.
class Details:
    # Class Attributes(Class Variable)...
    name = "Santanu Banik"
    age = 23

    # Constructor...
    def __init__(self):
        # Instance Attributes(Instance Variable)...
        self.name = "Banti"

    # Static method ...!
    @staticmethod
    def display():
        print(f"Name : {Details.name}")
        print(f"Age : {Details.age}")