# String slicing .......
# syntax : string_name[beginning(include): end(exclude) : step(optional)]


name = "Santanu Banik"
'''      
           S    a    n    t    a    n    u         B    a    n    i    k
index=>    0    1    2    3    4    5    6    7    8    9    10   11   12
index=>   -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
'''
print(f"name[ : ] : {name[:]}")
print(f"name[0:13] : {name[0:13]}")
print(f"name[:13] : {name[:13]}")
print(f"name[-13:12] : {name[-13:12]}")
print(f"name[-13:-1] : {name[-13:-1]}")

print(f"name[0:7] : {name[0:7]}")
print(f"name[0:] : {name[7:]}")
print(f"name[-13:-6] : {name[-13:-6]}")


print(f"name[0 : 13 : 2] : {name[0 : 13 : 2]}")