# Python program to demonstrate
# use of class method and static method.



class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    # a class method to create a Person class object.
    @classmethod
    def fromBirthYear(cls, _day, _month, _year,):
        print(f"Birth Day : {_day}/{_month}/{_year}")
        #return cls(_day, _month, _year)

    # a static method to check if a Person is adult or not.
    # @staticmethod
    # def isAdult(_age):
    #     if _age > 18:
    #         print(f"Name : {Person.name} is avobe 18")
    #     else:
    #         print(f"Name : {Person.name} is under 18")


# class Object ...
perObject = Person('Santanu Banik', 23)
print(f"type of perObject : {type(perObject)}")

perOther = Person.fromBirthYear( 15, "May", 1996)
print(f"type of perOther : {type(perOther)}")

#Person.isAdult(23)
#
# print(object.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))