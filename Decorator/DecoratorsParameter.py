# Decorators with parameters in Python ...!

def outerFunction(*args, **kwargs):

    print("outerFunction() call...")
    print(f"args :{args}")
    print(f"kwargs :{kwargs}")

    def innerFunction(argc):
        print("innerFunction() call...")
        print(f"Name : {kwargs['Name']}")
        print(f"Age : {kwargs['Age']}")
        return argc

    return innerFunction

tuple = (10,20,30,40,50)
dict = {'Name' : "Santanu Banik", 'Age' : 23}

@outerFunction(*tuple, **dict)
def display():
    print("Inside display() function")


display()