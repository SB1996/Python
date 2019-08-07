# if else Statement.....
'''
syntax : if condition :
            execute these statements
         else :
            execute these statements

'''
data00 = 10
data01 = 100

# Single if Statement
if data00 <= data01 :
    print(f"data01 : {data01} is Gteater Number.")


# Single if-else Statement
if data00 <= data01 :
    print(f"data01 : {data01} is Gteater Number.")
else :
    print(f"data00 : {data00} is Gteater Number.")


# Nested if-else Statement
if data00 <= 100 :
    if data00<=100 and data00>=75 :
        print(f"data00 : {data00} in range(100 to 75) ")
    elif data00<=75 and data00>=50 :
        print(f"data00 : {data00} in range(75 to 50) ")
    elif data00<=50 and data00>=25 :
        print(f"data00 : {data00} in range(50 to 25) ")
    elif data00<=25 and data00>=0 :
        print(f"data00 : {data00} in range(25 to 0) ")
    else :
        print(f"data00 : {data00} in out of range(0 to 100) ")

else :
    print(f"data00 : {data00} in out of range(0 to 100) ")



