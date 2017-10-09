# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.

# Get the number for the day of the week.
# be sure to format the input as an int

DAY_OF_WEEK = int(input('Please enter an integer of 1 to 7 to represent a weekday:'))

if DAY_OF_WEEK == 1: 
    print('The day of the week is Monday')
if DAY_OF_WEEK == 2:
    print('The day of the week is Tuesday')
if DAY_OF_WEEK == 3:
    print('The day of the week is Wednesday')
if DAY_OF_WEEK == 4:
    print('The day of the week is Thursday')
if DAY_OF_WEEK == 5:
    print('The day of the week is Friday')
if DAY_OF_WEEK == 6:
    print('The day of the week is Saturday')
if DAY_OF_WEEK == 7:
    print('The day of the week is Sunday')
elif DAY_OF_WEEK > 7:
    print('ERROR, Please enter an integer from 1 to 7.')


# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.



# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.