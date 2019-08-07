name = "Santanu"

'''      
         S  a  n  t  a  n  u
index=>  0  1  2  3  4  5  6
index=> -7 -6 -5 -4 -3 -2 -1
'''
# Accessing characters in Python
print(f"First Character[name] : {name[0]}")
print(f"First Character[name] : {name[-7]}")
print(f"Last Character[name] : {name[6]}")
print(f"Last Character[name] : {name[-1]}")

print(f"Name : {name}")
# re-assinged value
name = "Banti"
print(f"Changed Name : {name}")



string = "Santanu Banik"
print(f"String : {string}")
# Modify : String value...
# In python String are Immutable, so we cant modify string value
# string[0] = "B" # TypeError: 'str' object does not support item assignment
# del string[0] # TypeError: 'str' object doesn't support item deletion
string = "Banti Banik" # Here we can't modify string value, We refer another string(just change reference)
print(f"String : {string}")
del string # Here we can't delete string value, We delete refer of string(just delete reference)
# print(f"String : {string}")#NameError: name 'string' is not defined
# Have to initilize value before used variable
string = ""
print(f"String : {string}")


# String slicing .......
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




