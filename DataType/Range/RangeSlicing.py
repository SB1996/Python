# Range value slicing ...!
# Note :  Slicing Itarable Using Index value
rangeValue = range(1,21)

# Not Slicing ...
print("1. Full value : ",end=" ")
for i in rangeValue:
    print(i,end=" ")


# Value Slicing ...
print("\n2. Slicing value[0 to 20] : ",end=" ")
for i in rangeValue[:]:
    print(i,end=" ")


# Value Slicing ...
print("\n2. Slicing value[0 to 10] : ",end=" ")
for i in rangeValue[:10]:
    print(i,end=" ")


# Value Slicing ...
print("\n2. Slicing value[10 to 15] : ",end=" ")
for i in rangeValue[10:15]:
    print(i,end=" ")