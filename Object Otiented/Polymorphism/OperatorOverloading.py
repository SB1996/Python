# Operator Overloading in Python ...!


# Behind the seen in Python
# print(f"Addition : {10+20}")
# #       --or--
# print(f"Addition : {int.__add__(10, 20)}")
#
# print(f"Result : {'Santanu' + ' Banik'}")
# #      --or--
# print(f"Result : {str.__add__('Santanu', ' Banik')}")

class OverloadOperator:
    def __init__(self, arg):
        self.Data = arg

    # adding two objects ...
    def __add__(self, other):
        return self.Data + other.Data

obj00 = OverloadOperator(100)
obj01 = OverloadOperator(200)
print(obj00 + obj01)

strObj00 = OverloadOperator("Santanu ")
strObj01 = OverloadOperator("Banik")
print(strObj00 + strObj01)

##########################################

class complex:
    def __init__(self, arg00, arg01):
        self.arg00 = arg00
        self.arg01 = arg01

    # adding two objects ...
    # Overload '+' Operator
    def __add__(self, other):
        return self.arg00 + other.arg00, self.arg01 + other.arg01

    def __str__(self):
        return self.arg00, self.arg01

object00 = complex(10, 20)
object01 = complex(50, 60)
result = object00 + object01

# Behind the seen....in python ....
#
# object00 = complex(10, 20) ==> object00.arg00 = 10
#                                object00.arg01 = 20
#____________________________________________________

# object01 = complex(50, 60) ==> object01.arg00 = 50
#                                object01.arg01 = 60
#____________________________________________________

# object00 + object01 ==> __add__(object00, object01):
#                               return (object00.arg00 + object01.arg00, object00.arg01 + object01.arg01)
#                                       [(10 + 50), (20 + 60)] ==> (60, 80)
print(f"Result : {result}")


obj00 = complex("A", "B")
# obj00 = complex("A", "B") ==> obj00.arg00 = "A"
#                               obj00.arg01 = "B"

obj01 = complex("Z", "Y")
# obj01 = complex("Z", "Y") ==> obj01.arg00 = "Z"
#                               obj01.arg01 = "Y"

result00 = obj00 + obj01
print(f"Result : {result00}")