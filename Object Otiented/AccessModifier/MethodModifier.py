# Method visibility in Python ...!

class UserDetails:
    def __init__(self, name, user, pas):
        print("__init__() Block executed")
        self.name = name
        self._userName = user
        self.__password = pas


    # public method ...
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"UserName : {self._userName}")
        print(f"Password : {self.__password}")

    # private method ...
    def __showPassword(self):
        return self.__password

    # protected method ...
    def _showUser(self):
        print(f"UserName : {self._userName}")
        print(f"Password : {self.__password}")
        print(f"New Password : {self.__showPassword()}")


class User(UserDetails):
    pass

object = UserDetails("Santanu", "Santanu15", "***********")
object.showDetails()
userObject = User("Banti", "Banti05", "##########")
userObject.showDetails()
userObject._showUser()