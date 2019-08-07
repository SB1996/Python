# In Python, we can define a function inside another function.

# In Python, 'High Order Function' is a function can be passed as parameter to another function
# and function can also return another function.


def information(_name):
    print(f"information() call .....")
    print(f"Name : {_name}")
    return _name

#information("Santanu")

# High Order Function.
# highOrder() accept another function as a parameter.
# callback parameter is a function ...
def highOrder(args0, args1, callback):
    # data = callback()
    print(f"args0 : {args0}")
    print(f"args1 : {args1}")
    print(f"callback : {callback}")
    # print(f"data : {data}")
    # inner function ...
    def inner():
        # data00 = callback()
        # print(f"inside inner function data : {data}")
        return args0

    return inner

# high Order Function Call
cusFunction = highOrder(10, 20, information("Banti"))
cusValue = cusFunction()
print(f"cusValue : {cusValue}")