# Changing Class Members in Python ...!

# we have seen that Python doesn’t have static keyword. All variables that are assigned
# a value in class declaration are class variables.
# We should be careful when changing value of class variable.
# If we try to change class variable using object, a new instance (or non-static) variable for that particular
# object is created and this variable shadows the class variables.

class Student:
    Stream = "Information Technology" # Class Variable...
    # Constructor ...
    def __init__(self, name, id):
        self.Name = name
        self.Id = id

obj00 = Student("Santanu Banik", "IT007")
obj01 = Student("Atanu Banik", "CSE003")

# Before Changing Class Variable..........
print("Before Changing Class Variable...")
print(f"obj00.Stream : {obj00.Stream}")
print(f"obj01.Stream : {obj01.Stream}")
# print("####_id_####")
# print(f"id of (obj00.Stream) : {id(obj00.Stream)} ")
# print(f"id of (obj01.Stream) : {id(obj01.Stream)} ")
# print(f"id of (Student.Stream) : {id(Student.Stream)} ")
# print("####_id_####")
print("___________________________________________")
# After Changing Class Variable..........
# It change only for 'obj00' object and for other object it's still unchanged
obj00.Stream = "Computer Science & Engineering" # It's a new instance variable with same name
print("After Changing Class Variable...")
print(f"obj00.Stream : {obj00.Stream}")
print(f"obj01.Stream : {obj01.Stream}")
# Access by class name
print(f"Student.Stream : {Student.Stream}")
# print("####_id_####")
# print(f"id of (obj00.Stream) : {id(obj00.Stream)} ")
# print(f"id of (obj01.Stream) : {id(obj01.Stream)} ")
# print(f"id of (Student.Stream) : {id(Student.Stream)} ")
# print("####_id_####")


