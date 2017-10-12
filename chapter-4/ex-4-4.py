# Programming Exercise 4-4
#
# Program to show an hour-by-hour table of distances traveled for a given speed over a number of hours.
# This program accepts speed (in mph) and time traveled (in hours) from a user,
# then uses a loop to compute the cumulative distance traveled by each hour,
# and displays a table of results, which each hour on its own line 

# Declare variables for the distance, speed, and time.
# initialize these as integers

# Get the speed as input from the user and cast it appropriately.
    
# Get time traveled as input and cast it appropriately

# Display the table header: Hour and Distance separated by a tab
# Display an separator line composed of underscores

# Use a for loop to iterate over the range of hours

    # calculate the distance up to the current hour

    # Display the current hour and distance traveled, separated by a tab

distance = int
speed = int(input('Enter the speed at which you are traveling in MPH:'))
time = int(input('Enter the time traveled in hours:'))

print('Hour     Distance')
print('__________________')

for x in range(time+1):
    distance = x * speed
    print(x, '       ', distance, 'mi')