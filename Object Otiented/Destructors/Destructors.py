# Destructors in Python ...!

# Destructors are called when an object gets destroyed. In Python, destructors are not needed as much needed
# in C++ because Python has a garbage collector that handles memory management automatically.
# The __del__() method is a known as a destructor method in Python.
# It is called when all references to the object have been deleted i.e when an object is garbage collected.
# In python : [ Python has a garbage collector that handles memory management automatically ]


class Details:
    Name = "Banti"
    # Constructors (parameterized constructor)...
    def __init__(self, name):
        print("Constructor call ....")
        print(f"Name : {self.Name}")
        self.Name = name
        print(f"Name : {self.Name}")


    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Details object deleted.')


obj = Details("Santanu")
del obj

# Note : The destructor was called after the program ended or when all the references to object are deleted i.e when the
#        reference count becomes zero, not when object went out of scope.


class Information:

    # Constructors (default constructor)...
    def __init__(self):
        print("Constructor call ....")

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Information object deleted.')

def createObject():
    print('function start...')
    print('Making Object...')
    obj = Information()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
createObject()
print('Program End...')



# if your instances are involved in circular references they will live in memory for as long as the application run