# pass statement ...!

list = [0,1,2,3,4,5,6,7,8,9]

print("List : ",end=" ")
for i in list:
    if(i == 5):
        pass
    print(i,end=" ")

print("\n____________________________________")
#print("\nList : ",end=" ")
for i in list:
    for j in list:
        if ((i == 5)and(j == 5)):
            pass
        print(f"{i}:{j}",end=" ")
    print()