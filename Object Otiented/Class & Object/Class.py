# Defining a Class in Python ....!
#
# Class : A Class is a logical grouping of data and functions.(class is a User define data type)
#         It gives the freedom to create data structures that contains arbitrary content and hence easily accessible.
#
#         property : 1. Constructor
#                    2. Instance Attributes(Variable)
#                    3. Class Attributes(Variable)
#                    4. Methods



class Details:
    # Class Attributes(Class Variable)..
    name = "Santanu Banik"
    age = 23

    # Constructor..
    def __init__(self):
        fullName = "Santanu" # Local Attributes(Instance Variable)..
        self.name = "Banti" # Instance Attributes(Instance Variable)..

    # Methods..
    def showName(self):
        print(f"name : {self.name}")

# Creating instance of Class...
object = Details()
object.showName()# class method calling...