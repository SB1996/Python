# 1. Pass by Reference or pass by value?
# Ans : One important thing to note is, in Python every variable name is a reference.
#       When we pass a variable to a function, a new reference to the object is created.
#       Parameter passing in Python is same as reference passing in Java.


print("____________________________________________")
# When we pass a reference and modify value the received reference to something else,
# the connection between passed and received parameter is not broken
list = [10, 20, 30, 40, 50]
def modify(args):
    # Modify the value not change the reference
    args[0] = 0

print(f"Before Modify List : {list}")
modify(list)
print(f"After Modify List : {list}")

print("____________________________________________")
# When we pass a reference and change the received reference to something else,
# the connection between passed and received parameter is broken
list00 = [1,2,3,4,5]
def modifyReceived(args):
    # change the reference of 'args'

    args = [10,20,30,40,50]
    print(f"args List : {args}")


print(f"Before Modify List : {list00}")
modifyReceived(list)
print(f"After Modify List : {list00}")