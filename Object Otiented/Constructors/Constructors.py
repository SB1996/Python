# Constructors in Python ...!
#
# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values)
# to the data members of the class when an object of class is created.In Python the __init__() method is called
# the constructor and is always called when an object is created.

# Types of constructors : 1. default constructor : The default constructor is simple constructor which doesn’t accept
#                            any arguments.It’s definition has only one argument which is a reference to the instance
#                            being constructed.
#
#                         2. parameterized constructor : constructor with parameters is known as parameterized
#                            constructor. The parameterized constructor take its first argument as a reference
#                            to the instance being constructed known as self and the rest of the arguments are
#                            provided by the programmer.



class Details:
    Name = "Banti"
    # Constructors (parameterized constructor)...
    def __init__(self, name):
        print("Constructor call ....")
        print(f"Name : {self.Name}")
        self.Name = name
        print(f"Name : {self.Name}")


obj = Details("Santanu")