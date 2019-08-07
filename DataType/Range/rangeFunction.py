# Python - range Function ...!
# __________________________________________________________________________
# 1. range() function....
# [range() : This returns a list of numbers created using range() function.]
# [range() returns : the list as return type.]
# syntax :  range([start], stop, [step])
#           [statr] => optional parameter(include part)(defult value : 0)
#           [stop] => requeared parameter(exclude part)
#           [step] => optional parameter
#
# range(5) will generate 0,1,2,3,4
# range(1,10) will generate 1,2,3,4,5,6,7,8,9
# range(10,21,2) will generate 10,12,14,16,18,20
#
#________________________________________________________________________
#
# 2. xrange() function....[Present in python 2 not in python 3]
# [xrange() : This function returns the generator object that can be used to display numbers only by looping.]
# [xrange() returns : xrange() object.]


# 1. Using range() function ...!
# from pygments.util import xrange

rangeValue = range(1, 11)
print(f"rangeValue : {rangeValue}")
print("Itearate Value : ", end=" ")
for x in rangeValue:
    print(x, end=" ")
print(f"\nType : {type(rangeValue)}")

print("____________________________________________\n")

# 2. Using xrange() function ...!
# xrangeValue = xrange(1, 11)
# print(f"rangeValue : {xrangeValue}")
# print("Itearate Value : ", end=" ")
# for x in xrangeValue:
#     print(x, end=" ")
# print(f"\nType : {type(xrangeValue)}")










