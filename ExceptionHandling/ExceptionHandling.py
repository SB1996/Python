# Exception Handling in Python ...!
#
# Error : Compiling time Error( it's fix at compiling time )
# Exception : Run time Error( At run time we can't fix this, have to 'handle' it, to avoid unexpected out come )
#
#
# try except blocks :>  try :
#                             statements in try block ......
#                             Exception may or may be Occur
#                               if occur -> then, throw that Exception
#                               else nothing happen.
#                       except :
#                             executed when error in try block ......
#                                 if an Exception is throw by try block, then except that Exception
#                                 and handle it
#
#
# try  except else and finally :> try:
#                                     statements in try block ......
#                                     Exception may or may be Occur
#                                     ->if occur -> then, throw that Exception
#                                     ->else nothing happen.
#                                 except:
#                                      executed when error in try block ......
#                                      ->if an Exception is throw by try block, then except that Exception
#                                      and handle it
#                                 else:
#                                    executed if try block is error-free(Exception not occur).....
#                                    ->if an Exception not throw by try block, then else block executed
#                                 finally:
#                                       executed irrespective of exception occurred or not....
#                                       ->Exception may or may be Occur doesn't matter finally block always executed
#

data00 = int(input("Enter Value : "))
data01 = int(input("Enter Value : "))

try:
    result = data00//data01
    print(f"Result : {result}")
except ZeroDivisionError:
    print(f"An Exception occur ...\nException : divided by {data01}")
else:
    print(f"No Exception occur ...")
finally:
    print(f"finally block executed\nProgram end.....!")








