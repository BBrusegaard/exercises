# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.

# Get the person's age.
# remember to convert the input to an int.

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.

# display a message with the age category.

age = int(input('Please enter your age as an integer:'))

if age >= 18:
    print("You're an adult!")
if 18 > age >= 13:
    print("You're a teenager.")
if 13 > age >= 2:
    print("You're a child.")
if age < 2:
    print("You're an infant. How are you typing on a computer?")


    
    
