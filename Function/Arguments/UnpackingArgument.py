# Unpacking Argument Lists...!

def arbitraryArgument(*args):
    print(f"*args : {args}")
    print(f"type(*args) : {type(args)}")
    print(f"iterable value : ",end="")
    for i in args:
        print(i, end=" ")

arbitraryArgument(1, 2, 3, 4, 5)
print("\n__________________________________________")

tuple = (1, 2, 3, 4, 5)
list = [1, 2, 3, 4, 5]

arbitraryArgument(tuple)# Packing Argument Pass
print("\n__________________________________________")
arbitraryArgument(*tuple)# Unpacking Argument Pass
print("\n")
arbitraryArgument(*list)# Unpacking Argument Pass
