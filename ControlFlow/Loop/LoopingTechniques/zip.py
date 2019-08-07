# Using zip() ...!

'''
zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially.
The loop exists only till the smaller container ends. The detailed explanation of zip() and enumerate() can be found here.
'''

# python code to demonstrate working of zip()

# initializing list ...!
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'circle']
# using zip() to combine two[list] containers
# and print values
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))

print("\n____________________________________")
# initializing list ...!
name = ['Santanu', 'Partha', 'Souvik']
surName = ['Banik', 'Ghoshal', 'Mondal']
age = [23, 24, 26]

for i, j, k in zip(name, surName, age):
    print('{0} {1} age is : {2}'.format(i, j, k))


