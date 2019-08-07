# Default arguments ...!

def deteals(_fastName, _lastName):
    print(f"Name : {_fastName} {_lastName}")



deteals("Banti", "Banik")
deteals("Piku", _lastName = "Banik")
deteals(_fastName = "Santanu", _lastName = "Banik")
deteals(_lastName = "Banik", _fastName = "Santanu")


