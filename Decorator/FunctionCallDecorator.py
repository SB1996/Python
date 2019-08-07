def outerFunction(*args, **kwargs):

    def innerFunction(arg):
        print("before Execution")
        # getting the returned value
        #returned_value = args(*args, **kwargs)
        print("after Execution")
        # returning the value to the original frame
        return arg

    return innerFunction


# adding decorator to the function
@outerFunction
def addition(a, b):
    print("Inside the function")
    return a + b

data00 = 10
data00 = 20
# getting the value through return of the function
print(f"Sum : {addition(data00, data00)}")