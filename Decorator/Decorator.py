# Decorators in Python ...!
#
# In Python, functions are the first class objects.
#
# 1. Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# 2. Functions can be defined inside another function and can also be passed as argument to another function.
#
# Decorators : Decorators are very powerful and useful tool in Python since it allows programmers to modify
#              the behavior of function or class. Decorators allow us to wrap another function in order to extend
#              the behavior of wrapped function, without permanently modifying it.


# defining a function(OuterFunction)
def outerFunction(args):
    # inner1 is a Wrapper function in, which the argument is called
    print("outerFunction() call...")
    # inner function can access the outer local variable
    # defining a function(innerFunction)
    def innerFunction():
        print("innerFunction() call...")
        # calling the actual function now, inside the wrapper function.
        args()
        print("innerFunction() execution completed.")

    print("outerFunction() execution completed.")
    return innerFunction


# defining a function, to be called inside wrapper
# def outSideFunction():
#     print("outSideFunction() execution start")
#     #
#     #
#     #
#     print("outSideFunction() execution end")
#
#
# # passing 'outSideFunction' inside the outerFunction
# # decorator to control its behavior(change behavior outSideFunction)
# outSideFunction = outerFunction(outSideFunction)
# # calling the outSideFunction
# outSideFunction()

#    --or--
@outerFunction # invoked outerFunction when outSideFunction() call
def outSideFunction():
    print("outSideFunction() execution start")
    #
    #
    #
    print("outSideFunction() execution end")

outSideFunction();