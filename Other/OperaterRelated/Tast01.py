# Difference between '==' and 'is' operator in Python ....?
# Ans : The '==' operator compares the values of both the operands and checks for value equality.
#       Whereas 'is' operator checks whether both the operands refer to the same object or not.


list00 = [] # Empty list
list01 = [] # Empty list
list02 = list00 # Empty list by copy

print(f"list00 == list01 : {list00 == list01}") # True : list00 and list01 have same value(empty), {but refer to the different object}
print(f"list00 is list01 : {list00 is list01}") # False : list00 and list01 {have same value(empty)}, but refer to the different object

print(f"list00 == list02 : {list00 == list02}") # True : list00 and list01 have same value(empty), but refer to the same object
print(f"list00 is list02 : {list00 is list02}") # False : list00 and list01 have same value(empty), but refer to the same object

print("__________________________________")
data00 = 10
data01 = 10
# Same value and same reference ...!
print(f"data00 == data01 : {data00 == data01}")
print(f"data00 is data01 : {data00 is data01}")