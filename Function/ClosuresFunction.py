# Closures in Python ...!

# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
# A closure : unlike a plain function allows the function to access those captured variables through
#             the closure’s copies of their values or references, even when the function is invoked outside their scope.


# Python program to illustrate closures

# Outer function
def outerFunction(_text):
    print("Outer Function Call ...")
    text = _text
    print(f"Before Modify Data : {text}")

    # Inner function
    def innerFunction(_anotherText):
        print("Inner Function Call ...")
        text = _anotherText # Modify the Outer scope variable
        print(f"inner Function Modify Data : {text}")

    # print(f"After Modify Data : {text}")
    return innerFunction  # Note we are returning function WITHOUT parenthesis


myFunction = outerFunction("Hey! i'm Santanu")
myFunction("Hello Mr. Santanu")