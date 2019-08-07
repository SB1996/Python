# Nested Function ...!

# Python program to illustrate nested functions
def outerFunction(_text):
    text = _text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey! i\'m Santanu')