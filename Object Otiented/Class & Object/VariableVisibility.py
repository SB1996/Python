# Variable visibility in Python ....!

class Visibility:
    def __init__(self):
        pass

    staticData = "class : visibility => Static Data Member"
    def visibal(self):
        localData = "class : visibility => Local Data Member"
        self.instanceData = "class : visibility => Instance Data Member"

        print(f"{Visibility.staticData}") # Accessed...
        print(f"{self.instanceData}")# Accessed...
        print(f"{localData}")# Accessed....

    def accessed(self):
        print(f"{Visibility.staticData}")# Accessed...
        print(f"{self.instanceData}")# Accessed...
        # print(f"{localData}")# Not Accessed....


obj = Visibility()
obj.visibal()
print("______________________________________________")
obj.accessed()