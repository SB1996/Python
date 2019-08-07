# intData = 10
# print(f"Int -> Hexadecimal : {hex(intData)}")
# print(f"Int -> Octal : {oct(intData)}")
# print(f"Int -> Float : {float(intData)}")
# print(f"Int -> String : {str(intData)}")
#
#
# strinngData = "10010"
# print(f"String -> Float : {float(strinngData)}")
# print(f"String -> Int : {int(strinngData)}")
#
# charData = 'S'
# print(f"String(Char) -> Int : {ord(charData)}")


# String -> List, Tuple, Set
strData = "Santanu"

print(f"String -> List : {list(strData)}")
print(f"String -> Tuple : {tuple(strData)}")
print(f"String -> Set : {set(strData)}")

# List ->  Tuple, Set, Dictionary
listData = [1,2,3,4,5]
listData00 = [['one', 100], ['two', 200], ['three', 300]]
print(f"List -> Tuple : {tuple(listData)}")
print(f"List -> Set : {set(listData)}")
print(f"List -> List : {dict(listData00)}")

# Tuple ->  List, Set, Dictionary
tupleData = (1,2,3,4,5)
tupleData00 = (('one', 100), ('two', 200), ('three', 300))
print(f"Tuple -> List : {list(listData)}")
print(f"Tuple -> Set : {set(listData)}")
print(f"Tuple -> Dictionary : {dict(listData00)}")








