# Duck typing in Python ....!

# Class one....
class Drive00:

    def executed(self):
        print("Drive00 executed call....")
# Class another ....
class Drive01:

    def executed(self):
        print("Drive01 executed call....")

objDrive00 = Drive00()
objDrive01 = Drive01()
# Here two class have same method(executed).....
class Duck:
   def run(self,object):
       object.executed()


objDuck = Duck()
objDuck.run(objDrive00) # Duck typing
objDuck.run(objDrive01) # Duck typing