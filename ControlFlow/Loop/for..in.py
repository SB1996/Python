# for..in Loop....!
'''
syntax : for iterator_var in sequence:
             statements(s)

'''
import array as pyarray


# List
list = [1,2,3,4,5,6,7,8,9,0]
print("List : ",end=" ")
for i in list:
    print(i,end=" ")
print("\n____________________________________")
# Array
array =  pyarray.array('i',[0,1,2,3,4,5,6,7,8,9]) # signed int type Array
print("\nArray : ",end=" ")
for i in range(0,10) :
    print(array[i], end=" ")
print("\nArray : ",end=" ")
for i in array :
    print(i, end=" ")

print("\n____________________________________")
# Iterating by index of sequences...!
list = ["Santanu", "Banti", "Piku"]
print("\nList : ",end=" ")
for index in range(len(list)):
    print(list[index],end=" ")

print("\n____________________________________")
# Using else statement with for loops ...!
list = ["Santanu", "Banti", "Piku"]
print("\nList : ",end=" ")
for index in range(len(list)):
    print(list[index],end=" ")
else:
    print("\nInside Else Block")