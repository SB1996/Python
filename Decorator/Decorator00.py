# What if a function returns something :

# defining a function(OuterFunction)
def outerFunction(arg):
    # inner1 is a Wrapper function in, which the argument is called
    print("outerFunction() call...")

    # inner function can access the outer local variable
    # defining a function(innerFunction)
    def innerFunction(*args, **kwargs):
        print("innerFunction() call...")

        # getting the returned value
        returnValue = arg(*args, **kwargs)

        print("innerFunction() execution completed.")
        return returnValue

    print("outerFunction() execution completed.")
    return innerFunction



# adding decorator to the function
@outerFunction
def addition(a, b):
    print("Inside the addition() function")
    return (a + b)

data00 = 10
data00 = 20
# getting the value through return of the function
print(f"Sum : {addition(data00, data00)}")