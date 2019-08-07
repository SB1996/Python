# Arbitrary Argument List ...!


# 1. Arbitrary Argument List Using '*args'...!
def arbitraryArgument(*args):
    print(f"*args : {args}")
    print(f"type(*args) : {type(args)}")
    print(f"iterable value : ",end="")
    for i in args:
        print(i, end=" ")
# call the function with 5 argument
arbitraryArgument(1, 2, 3, 4, 5)
print("\n__________________________________________")
arbitraryArgument("Santanu", "Banti", "Piku")
print("\n__________________________________________")
arbitraryArgument(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("\n============================================\n")
def arbitraryArgument00(args00, *args, args01 = 100):
    print(f"*args : {args}")
    print(f"args00 : {args00}")
    print(f"args01 : {args01}")
    print(f"type(*args) : {type(args)}")
    print(f"iterable value : ",end="")
    for i in args:
        print(i, end=" ")
arbitraryArgument00(10, 20,30,40,50)

print("\n============================================\n")
def arbitraryArgument01(args00, *args, args01):
    print(f"*args : {args}")
    print(f"args00 : {args00}")
    print(f"args01 : {args01}")
    print(f"type(*args) : {type(args)}")
    print(f"iterable value : ",end="")
    for i in args:
        print(i, end=" ")

arbitraryArgument01(10, 20,30,40,50, args01= 200)


print("\n\n============================================")
print("============================================\n")
# 2. Arbitrary Argument List Using '**args'...!
def arbitraryArgument000(**kwargs):
    print(f"**args : {kwargs}")
    print(f"type(*args) : {type(kwargs)}")
    print(f"iterable value : ",end="")
    for i in kwargs:
        print(f"{i}=>{kwargs[i]}", end=" ")


arbitraryArgument000(one = "Santanu", two = "Banti", three = "Piku")
