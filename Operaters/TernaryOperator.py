# Ternary Operator ...!

# Syntax : [on_true] if [expression] else [on_false]

# 1. Simple Method to use ternary operator :
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)



# Program to demonstrate conditional operator
a, b = 10, 20
# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)