# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.
speed = float(50.523)

# Constant for the speed.
t1 = float(6*speed)
t2 = float(10*speed)
t3 = float(15*speed)

# Calculate the distance the car will travel in
# 6, 10, and 15 hours.

# Print the results for all calculations.
print('The car will travel' , format(t1, ".2f"), 'miles in 6 hours')
print('The car will travel' , format(t2, ".2f"), 'miles in 10 hours')
print('The car will travel' , format(t3, ".2f"), 'miles in 15 hours')



