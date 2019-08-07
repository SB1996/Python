# Python code to demonstrate range() vs xrange()
# on  basis of memory

import sys
# from ipython_genutils.py3compat import xrange
from pygments.util import xrange

# initializing a with range()

a = range(1, 10000)

# initializing a with xrange()
x = xrange(1, 10000)

# testing the size of a
# range() takes more memory
print("The size allotted using range() is : ",end="")
print(sys.getsizeof(a))

# testing the size of a
# range() takes less memory
print("The size allotted using xrange() is : ",end="")
print(sys.getsizeof(x))