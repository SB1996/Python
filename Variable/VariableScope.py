
# Global Variable....!
name = "Global Variable Scope"
print(f"Global field : {name}")

def display() :
    # Local Variable....!
    name  = "Loacl Variable Scope"
    print(f"Local field : {name}")

display()
print(f"Global field : {name}")

def show() :
    global name
    print(f"Local field : {name}")

show()
