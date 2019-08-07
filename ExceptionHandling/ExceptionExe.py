try:
    data00 = int(input("Enter Value : "))
    data01 = int(input("Enter Value : "))
    result = data00//data01
    print(f"Result : {result}")

except ZeroDivisionError:
    print(f"An Exception occur 'ZeroDivisionError'\nException : divided by {data01}")
except ValueError:
    print(f"An Exception occur 'ValueError' and Handled")
except:
    print(f"An Exception occur")

else:
    print(f"No Exception occur ...")

finally:
    print(f"finally block executed\nProgram end.....!")