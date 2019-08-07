# Function Decorators in Python ...!
#
# Function Decorator : A decorator is a function that takes a function as its only parameter and returns a function.
#                      This is helpful to “wrap” functionality with the same code over and over again. For example,
#                      above code can be re-written as following.

# Adds a welcome message to the string returned by fun(). Takes fun() as  parameter and returns welcome().
def message(fun):
    # Nested function
    def welcome(argument):
        return "Welcome to " + fun(argument)

    # Decorator returns a function
    return welcome


@message
def site(args):
    return args;


# Driver code

# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("python programming"))
