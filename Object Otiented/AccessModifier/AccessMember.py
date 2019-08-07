# Access Modifier/Specifier in python ...!
#
# Access modifier : 1. public
#                   2. private
#                   3. protected
#
# public : The members declared as Public are accessible from outside the Class through an object of the class.
#          [ By default, all the variables and member functions of a class are public in a python program. ]
#
# private : These members are only accessible from within the class. No outside Access is allowed.
#           [ While the addition of prefix __(double underscore) results in a member variable or function becoming private ]
#
# protected : The members declared as Protected are accessible from outside the class
#             but only in a class derived from it that is in the child or subclass.
#             [ According to Python convention adding a prefix _(single underscore) to a variable name makes it protected.
#             Yes, no additional keyword required. ]



class Details:
    # public attribute...
    name = "Santanu Banik" # public class variable[satatic variable]
    # protected attribute...
    _email = "santanu.banik1996@gmail.com" # protected class variable[satatic variable]
    # private attribute...
    __userName = "Santanu15" # private class variable[satatic variable]
    __password = "**********" # private class variable[satatic variable]

    # public instance method ...!
    def getEmail(self):
        return Details._email

    # public instance method ...!
    def getUser(self):
        return Details.__userName


    # public instance method ...!
    def getPassword(self):
        return Details.__password


#inhatited Details Class...into Santanu class
class Santanu(Details):
    pass



objectDetails = Details()
print(f"Name : {objectDetails.name}")
print(f"Email : {objectDetails.getEmail()}")

print("_______________________________________________")
objectSantanu = Santanu()
print(f"Email : {objectSantanu.getEmail()}")
print(f"UserName : {objectSantanu.getUser()}")
print(f"Password : {objectSantanu.getPassword()}")
