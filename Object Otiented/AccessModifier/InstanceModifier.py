# Instance "Access Modifier" data member(variable) in Python...!

class Details:
    def __init__(self):
        print(f"__init__ block start")
        # local variable
        publicData00 = "public ststic Data" # public data attribute.
        _protectedData00 = "protected ststic Data" # protected data attribute.
        __privateData00 = "private ststic Data" # private data attribute.
        print(f"{publicData00}")
        print(f"{_protectedData00}")
        print(f"{__privateData00}")
        print("\n")
        # class instance variable
        self.publicData01 = "public ststic Data"  # public data attribute.
        self._protectedData01 = "protected ststic Data"  # protected data attribute.
        self.__privateData01 = "private ststic Data"  # private data attribute.
        print(f"{self.publicData01}")
        print(f"{self._protectedData01}")
        print(f"{self.__privateData01}")

        print(f"__init__ block end ...!")




objectDetails = Details()

# Access [public, protected, private] member variable Outside of the class
# Using class name not object....
print("__________________________________________________")
print(f"Using 'instance' : {objectDetails.publicData01} Accessed")
print(f"Using 'instance' : {objectDetails._protectedData01} Accessed")
print(f"Using 'instance' : {objectDetails._Details__privateData01} Accessed")