# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
tract = float(input('What is the size of the tract in square feet?'))           #Prompts user for the size of their tract in sq ft

# Constant for the number of square feet in an acre.
SQUARE_FEET_IN_ACRES = 43560                                                    #All caps sets sq ft in acres as a constant (1sqft = 43560 acres)

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
acres = tract / 43560                                                           #Divides the variable tract by the constant 43560

# Calculate the number of acres.

# Print the number of acres.
# remember to format the acres to two decimal places

print('The tract is' , format(acres, ".2f"), 'acres in size.')                  #Prints statement "The tract is" then formats calculation to two float values




