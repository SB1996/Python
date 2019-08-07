# Special operators: There are some special type of operators like :
#     1. Identity operators
#     2. Membership operators
data00 = 100
data01 = '100'

# 1. Identity operators ...!
# Identity operators : is and is not are the identity operators both are used to check if two values are located on the same part of the memory.
#                      Two variables that are equal does not imply that they are identical
#
#                       is          True if the operands are identical
#                       is not      True if the operands are not identical
print(f"data00 is data01 : {data00 is data01}")
print(f"data00 is not data01 : {data00 is not data01}")

# 2. Membership operators ...!
# Membership operators : in and not in are the membership operators; used to test whether a value or variable is in a sequence.
#
#                        in            True if value is found in the sequence
#                        not in        True if value is not found in the sequence
data00 = [1,2,3,4,5,6,7,8,9,10]
data01 = 10

print(f"data01 in data00 : {data01 in data00}")
print(f"data01 not in data00 : {data01 not in data00}")
