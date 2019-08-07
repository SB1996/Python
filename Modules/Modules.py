# Python Modules ...!
#
# A module is a file containing Python definitions and statements. A module can define functions,
# classes and variables. A module can also include runnable code. Grouping related code into a module
# makes the code easier to understand and use.

from CustomModule import addition as sum

data = (1,2,3,4,5)
print(f"Result : {sum(*data)}")
