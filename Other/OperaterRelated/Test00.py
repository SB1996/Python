# Python | a += b is not always a = a + b....!
#
# In python a += b doesn’t always behave the same way as a = a + b,
# same operands may give the different results under different conditions...


list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]

print(f"list1 : {list1}")
print(f"list2 : {list2}")
# expression list1 += [1, 2, 3, 4] modifies the list in-place, means it extends the list
# such that “list1” and “list2” still have the reference to the same list.

print("______________________________________")

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

print(f"list1 : {list1}")
print(f"list2 : {list2}")
# expression list1 = list1 + [1, 2, 3, 4] creates a new list and changes “list1” reference to that new list
# and “list2” still refer to the old list.