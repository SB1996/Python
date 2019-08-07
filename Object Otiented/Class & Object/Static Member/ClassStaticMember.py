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

    @classmethod
    def show(cls):
        print(f"Name : {Details.name}")
        print(f"Age : {cls.age}")

    @staticmethod
    def display():
        print(f"Name : {Details.name}")
        print(f"Age : {Details.age}")
    #________________________________________________________________

# Creating instance of Class Details...
object = Details()

# call class instance method ...
object.showName() # method calling...
print("________________________________")
# call class static method ...
Details.show() # method calling...