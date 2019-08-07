# Taking input in Python ...!
#
# Python provides us with two inbuilt functions to read the input from the keyboard : 1. raw_input ( prompt )
#                                                                                     2. input ( prompt )
#
# 1. raw_input ( ) : This function works in older version (like Python 2.x). This function takes exactly what is typed
#                    from the keyboard, convert it to string and then return it to the variable in which
#                    we want to store.
#                    ->return type : String
#
# 2. input ( ) : This function first takes the input from the user and then evaluates the expression,
#                which means Python automatically identifies whether user entered a string or a number or list.
#                If the input provided is not correct then either syntax error or exception is raised by python.
#                ->return type : String

data = input("Enter any value : ")
print(f"type of data : {type(data)}")
print(f"data : {data}")
