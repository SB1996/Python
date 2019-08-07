# Generators in Python...!
#
# 1. Generator-Function : A generator-function is defined like a normal function, but whenever it needs to
#                      generate a value, it does so with the yield keyword rather than return. If the body of a def
#                      contains yield, the function automatically becomes a generator function.


# A generator function that yields : 1 for first time
#                                    2 for second time
#                                    3 for third time
#                                    4 for fourth time
#                                    5 for fifth time
def generatorFunction():
    print("generator function is call....")
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Driver code to check above generator function
for value in generatorFunction():
    print(value,end=" ")


# 2. Generator-Object : Generator functions return a generator object. Generator objects are used either by calling
#                       the next method on the generator object or using the generator object in a “for in” loop
#                       (as shown in the above program).
def generatorObject():
    print("\ngenerator function is call....")
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

object = generatorObject()
print()
print(object,end=" ")
print(object.__next__(),end=" ")
print(object.__next__(),end=" ")
print(object.__next__(),end=" ")
print(object.__next__(),end=" ")
print(object.__next__(),end=" ")