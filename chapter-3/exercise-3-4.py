# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.

# Get number from user and convert it to an int
numeral = int(input('Please enter a number from 1 to 10 to be converted to a Roman numeral:'))
# Set numeral to a Roman numeral value based on the value of number
if numeral == 1:
    print('Roman numeral 1 is: I')
if numeral == 2:
    print('Roman numeral 2 is: II')
if numeral == 3:
    print('Roman numeral 3 is: III')
if numeral == 4:
    print('Roman numeral 4 is: IV')
if numeral == 5:
    print('Roman numeral 5 is: V')
if numeral == 6:
    print('Roman numeral 6 is: VI')
if numeral == 7:
    print('Roman numeral 7 is: VII')
if numeral == 8:
    print('Roman numeral 8 is: VIII')
if numeral == 9:
    print('Roman numeral 9 is: IX')
if numeral == 10:
    print('Roman numeral 10 is: X')
# use a set of if ... elif .... etc. statements.
else:
    print('ERROR... NUMBER OUT OF RANGE')

# use a final else to display an error if number is out of range.


# display the numeral on the screen.






