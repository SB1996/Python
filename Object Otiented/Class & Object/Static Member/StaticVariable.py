# Static/Class variable in python ...
#
# Static/Class Variable :  Class or static variables are shared by all objects.
#                          (static variable are always same for every class's object)

# Non-static Variable : Instance or non-static variables are different for different objects
#                       (every object has a copy of it)
#                       (non-static variable are different for every class's object).
class StudentDetails:
    # static variavles ...
    collegeName = ""
    # constructor ...
    def __init__(self):
        print("Class constructor : called")

    # Instance method ...
    def setCollege(self,_clgName):
        print(f"{_clgName} object : CREATED")
        StudentDetails.collegeName = _clgName

    def details(self, _name, _classId,):
        self.name = _name
        self.id = _classId

    def otherDetails(self, _stream, _depId):
        self.stream = _stream
        self.depertId = _depId

    def show(self):
        print("_______________________________________________")
        print(f"College Name : {StudentDetails.collegeName}")
        print(f"Name : {self.name}")
        print(f"Class Id : {self.id}")
        print(f"Stream : {self.stream}")
        print(f"Department Ide : {self.depertId}")


# Create object for B.C.E.T Durgapur
bcetObject = StudentDetails()
# set the College Name
bcetObject.setCollege("B.C.E.T Durgapur")

bcetObject.details("Santanu Banik", 100792)
bcetObject.otherDetails("Information Technology", "IT007")
bcetObject.show() # Display the Details

atanuObject = StudentDetails()
atanuObject.details("Atanu Banik", 100666)
atanuObject.otherDetails("Information Technology", "IT007")
atanuObject.show() # Display the Details