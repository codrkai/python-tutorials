''' github.com/codrkai
this is a comment using single quotes
it requires three single quotes
and it allows comments on mutiple lines
'''

"""
this is another comment but using three double quotes
and is also a multiline comment
"""

# How to declare variables
# all variable declarations must contain a character first!
# ex. this is invalid: 123myvar - because it contains a number first.
# this will work: my123var or myvar123

myVar = 'orange' # variable names are case sensitive
myvar = "purple" # this variable name is different from the one above, even though its spelled the same


# Variables and string concatenation

str0 = "blue" # this is a single line comment. this variable uses double quotes as a string
str1 = 'red' # this variable uses a single quote for the string
str2 = str0 + ' and ' + str1 # this variable is now equal to: blue and red


# There are many print functions!

print('the sky is ' + str0) # this will output: the sky is blue
print('the sky is {} and {}'.format(str0, str1)) # this will output: the sky is blue and red
print('the sky is {1} and {0}'.format(str0, str1)) # this will output: the sky is red and blue
print('the sky is', str0) # this will print the sky is blue
print(f'the sky is {str1}') # notice the f! this will output: the sky is red


# If then else syntax! Remember to indent correctly!

if str0 != str1:
    if str0 == 'blue':
        print('yes')
else:
    print('these strings match')


# Capturing user input

myvar = input('What color is the sky? ') # when executed, the computer will wait for user to type an input

# the if statement below will convert the variables to lower case, then compare them
if myvar.lower() == str0.lower():
    print('yes the sky is blue')
else:
    print('no you stupid')


# Simple math and type casting

num_pi = 3.14
num_subscribers = '1000' # I've intentionally set this to a string. Below, I will change it back to an int()
total = (num_pi * int(num_subscribers)) / 2
print(total)


'''
www.github.com/codrkai
'''
