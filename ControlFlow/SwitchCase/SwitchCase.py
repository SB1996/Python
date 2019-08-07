# switch Case statement dose't support in python.
#
# Q. What is the replacement of Switch Case in Python ?
# Ans : Unlike every other programming language we have used before,
#       Python does not have a switch or case statement. To get around this fact, we use dictionary mapping.

# Function to convert number into string
# Switcher is dictionary data type here
def days(argument):
    switcher = {
        0: "Sunday",
        1: "MonDay",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")


# Driver program
if __name__ == "__main__":
    argument = 3
    print(f"Day : {days(argument)}")