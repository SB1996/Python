# userInput generator ...!
generator = (int(x) for x in input("Enter value : ").split())
print(f"generator : {generator}")
print(f"type of generator : {type(generator)}")
print(f"generator : {generator.__next__()}")
print(f"generator : {generator.__next__()}")
print(f"generator : {generator.__next__()}")
print(f"generator : {generator.__next__()}")
print(f"generator : {generator.__next__()}")
