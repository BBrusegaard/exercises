# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.

# Global constants for minimum, maximum and mass multiplier values

# Variables for weight and mass initialized as floats
# Get mass from user and convert it to a float
# Calculate weight using the mass multiplier constant

mass = float(input('Enter a mass in kilograms to be converted to Newtons:'))
minimum = 100
maximum = 1200
weight = (mass * 9.81)

float(weight)
float(mass)

if weight >= maximum:
    print(format(weight, ".2f") , 'Newtons is too large!')
if weight <= minimum:
    print(format(weight, ".2f") , 'Newtons is too small!')
else:
    print(format(weight, ".2f") , 'Newtons')
# Display the weight
# If weight > maximum or < than minimum display an appropriate message









