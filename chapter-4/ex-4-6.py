# Programming Exercise 4-6
#
# Program to display a table of Celsius and Fahrenheit equivalents.
# This program takes no input.
# It calculates a series of Fahrenheit equivalents for a range of Celsius temperatures
# then displays them in a table.

# Declare a float variable to hold the Fahrenheit temperature.

# Declare a constant to hold the max celsius value

# Display a table header with Celsius and Fahrenheit separated by two tabs.
# Display a line separator made of underscores

# Use a for loop to iterate from 0 through the range of Celsius temperatures

# 	Calculate the Fahrenheit temperature for the current Celsius value

#	Display the current Celsius and Fahrenheit values, separated by two tabs

fahrenheit = 0.0
MAX_CELSIUS = float
MAX_CELSIUS = 15

print('Celsius       Fahrenheit')
print('________________________')

for x in range(0, MAX_CELSIUS+1):
    fahrenheit = x * 1.8 + 32
    print(x, '          ', format(fahrenheit, ".2f"))