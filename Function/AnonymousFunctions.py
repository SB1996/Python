# Anonymous Function(lambda  function / lambda expression) in Python ...!

# In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to
# define the normal functions and the lambda keyword is used to create anonymous functions
#
# syntax :=> lambda arguments: expression

# Q.1> difference between a normal def defined function and lambda function?
# Ans : 1. This function can have any number of arguments but only one expression, which is evaluated and returned.
#       2. One is free to use lambda functions wherever function objects are required.
#       3. You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#       4. It has various uses in particular fields of programming besides other types of expressions in functions.

# Function declaration ...
def returnQube(args):
    return (args*args*args)
print(f"Result : {returnQube(10)}")

# lambda expression ...
qube = lambda args: (args*args*args)
print(f"Result : {qube(5)}")
