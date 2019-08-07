# Function Decorator in Python.

# A decorator is a function that takes a function as its only parameter and returns a function.
# This is helpful to “wrap” functionality with the same code over and over again

# For example, below code can be re-written as following.
# Adds a welcome message to the string returned by callback().
# Takes callback() as parameter and returns welcome(). 
def decorateMessage(callback):
    # Nested function ...
    def welcomeMassage(_massage):
        return "Welcome in " + callback(_massage)

    # Decorator returns a function
    return welcomeMassage


@decorateMessage
def showMassage(_massage):
    return _massage;


# Driver code 

# This call is equivalent to call to decorateMessage() with function 
# showMassage("GeeksforGeeks") as parameter 
print(showMassage("Python Language"))