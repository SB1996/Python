

class Details:
    # Class Attributes(Class Variable)...
    name = "Santanu Banik"
    age = 23

    # Constructor...
    def __init__(self):
        # Instance Attributes(Instance Variable)...
        self.name = "Banti"

    # Methods...
    def showName(self):
        print(f"name : {self.name}")

# Creating instance of Class...
object = Details()

# class method calling...
Details.showName(object)
#     --or--
object.showName()