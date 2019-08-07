# Instance variable in python ...!

class Student:
    def __init__(self, name):
        self.fullName = name
        print(f"Id Name : {id(self.fullName)}",end=" ")
        print(f"Name : {self.fullName}")


    def change(self, name):
        print(f"Id Name : {id(self.fullName)}",end=" ")
        print(f"Name : {self.fullName}")
        self.fullName = name
        print(f"Id Name : {id(self.fullName)}",end=" ")
        print(f"Name : {self.fullName}")


obj = Student("Santanu")
print("______________________________________")
obj.change("Banti")