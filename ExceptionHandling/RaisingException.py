# Raising Exception : The 'raise' statement allows the programmer to force a specific exception to occur.
#                     The sole argument in raise indicates the exception to be raised.
#                     This must be either an exception instance or
#                     an exception class(a class that derives from Exception).

try:
    raise NameError("NameError Forcefully throw(raise) by User.")  # Raise Error
except NameError:
    print("An Exception(NameError) Detecet : ")
    raise  # To determine whether the exception was raised or not
