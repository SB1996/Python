# Taking multiple inputs from user in Python ...!

# Developer often wants a user to enter multiple values or inputs in one line. In C++/C user can take multiple inputs in
# one line using scanf but in Python user can take multiple values or inputs in one line by two methods.
#
# 1. Using split() method
# 2. Using List comprehension(taking input as a List)
#
#
# 1. split() method : This function helps in getting a multiple inputs from user . It breaks the given input by
#                           the specified separator. If separator is not provided then any white space is a separator.
#                           Generally, user use a split() method to split a Python string but one can used it in taking
#                           multiple input.
#
#                           Syntax : input().split(separator=" ", maxsplit)
#                                                  separator by default space


data00 ,data01, data02 = input("Enter 3 integer value separate by space : ").split(" ")
print(f"data00 : {data00}")
print(f"data01 : {data01}")
print(f"data02 : {data02}")

