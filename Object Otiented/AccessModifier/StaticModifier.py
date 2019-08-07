# Static "Access Modifier" data member(variable) in Python...!


class Information:
    # those data(variable) are not act like proper 'Access Modifier'

    # public data attribute.
    publicData = "public ststic Data"
    # protected data attribute.
    _protectedData = "protected ststic Data"
    # private data attribute.
    __privateData = "private ststic Data"

# Access [public, protected, private] member variable Outside of the class .........
# Using class name not object....
print(f"Using 'class' : {Information.publicData} Accessed")
print(f"Using 'class' : {Information._protectedData} Accessed")
print(f"Using 'class' : {Information._Information__privateData} Accessed")

print("__________________________________________________")
# instance of Class
object = Information()
# Access [public, protected, private] member variable Outside of the class .........
# Using instance/object....
print(f"Using 'instance' : {object.publicData} Accessed")
print(f"Using 'instance' : {object._protectedData} Accessed")
print(f"Using 'instance' : {object._Information__privateData} Accessed")
