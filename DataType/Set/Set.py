'''
In Python, Set is an unordered collection of difference type of 'data' that is iterable, mutable and can't contain duplicate elements.
'''

# Set declaration......
set00 = set() # empty Set declaration

'''
Note : Sets are a useful tool for preserving a sequence of data and further iterating over it.
Note : Set elements are mutable.
Note : Set can't contain duplicate elements.
Note : Set contain only one iterable(object) elements(String,List,Tuple,Set).
Note : Set is an unordered collection.
'''

set01 = set("ABCDEFGH") # Contain String
print(f"set01 : {set01}")

set02 = set([1,2,3,4,5]) # Contain List
print(f"set02 : {set02}")

set03 = set((1,2,3,4,5)) # Contain Tuple
print(f"set03 : {set03}")

set04 = set(set02) # Contain Set
print(f"set04 : {set04}")

set05 = set(["Santanu", 10, 10.00, True]) # Contain List
print(f"set05 : {set05}")

set06 = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
print(f"set06 : {set06}")

set07 = set(((1,2,3,4,5), (3,6,6), (6,8,9,6,4,3,3,)))
print(f"set07 : {set07}")



