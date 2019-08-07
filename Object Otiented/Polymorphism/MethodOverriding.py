# Method Overriding in Pyrthon ....!

class DeriveClass:
    def __init__(self):
        print("DeriveClass class __init__() call ...")

    def show(self):
        print("DeriveClass class show() call ...")


class SubClass(DeriveClass):
    def __init__(self):
        super().__init__()
        print("SubClass class __init__() call ...")

    # override method
    def show(self):
        print("SubClass class show() call ...")


subObj = SubClass()
subObj.show()