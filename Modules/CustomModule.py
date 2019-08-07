# Addition function ...!
def addition(*args):
    value = 0
    for i in args:
        value = value + i

    return value


if __name__ == '__main__':
    data = (10, 20, 30, 40, 50)
    print(f"Result : {addition(*data)}")
