# Array in Python....!

'''
[(TYPE) (C TYPE)	(PYTHON TYPE)	(MINIMUM SIZE IN BYTES) ]
‘b’	signed char	             int	1
‘B’	unsigned char	         int	1
‘u’	Py_UNICODE	             unicode character	2
‘h’	signed short	         int	2
‘H’	unsigned short	         int	2
‘i’	signed int	             int	2
‘I’	unsigned int	         int	2
‘l’	signed long	             int	4
‘L’	unsigned long	         int	4
‘q’	signed long long         int	8
‘Q’	unsigned long long       int	8
‘f’	float	                 float	4
‘d’	double	                 float	8

'''
#
'''
Note : Array are not fixed size.
Note : Array elements Are mutable.
'''


# importing "array module" for array operations
# Syntax : array(data type, value list)
import array as pyarray

array =  pyarray.array('i',[0,1,2,3,4,5,6,7,8,9]) # signed int type Array

for i in range(0,10) :
    print(array[i], end=" ")

array[5] = 0 # Modify array element...
print()
for i in range(0,10) :
    print(array[i], end=" ")


# using insert() to insert value at specific position
# inserts 5 at 2nd position
array[5] = 5 # Modify array element...
print()
array.insert(10, 10)# Modify array size & value
for i in range(0,11) :
    print(array[i], end=" ")

