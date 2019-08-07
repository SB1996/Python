# Iterators in Python ...!

# iterating over a String..
name = "Santanu Banik"
print("\nName : ",end="")
for i in name:
    print(i,end="")

# iterating over a list..
nameList = ["Santanu","Banti", "Partho", "Biki", "Banka", "Titu"]
print("\nName : ",end="")
for i in nameList:
    print(i,end=" ")

# iterating over a tuple..
number = (10, 20, 30, 40, 50)
print("\nNumber : ",end=" ")
for i in number:
    print(i,end=" ")

# Iterating over dictionary..
dist = {1: "Banti",2: "Biki", 3: "Banka"}
print("\n")
for i in dist:
    print(f"{i} : {dist[i]}")
