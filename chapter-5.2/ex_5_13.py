# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
# 	that returns the falling distance for that amount of time,
# and displays the results as a table.

# define the main function

    # define a local float variable to hold distance
    
    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
#Time   Distance
#_______________
    
    # loop through a range of time values (in seconds)

        # pass the time to a falling distance function and assign result to distance

		# print the time and distance formatted to two places, separated by a tab

# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time

	# define a local float variable to hold falling distance
	
	# compute the falling distance using a formula and the time
	
	# return the falling distance

# Call the main function to start the program
from tables import print_two_column_header

def main():
    distance = 0.0
    time = 0.0
    print_two_column_header("Time", "Distance")
    global x
    for time in range(31):
        print(time,'sec','  ',format(falling_distance(time, distance),'.2f'),'m')
        
def falling_distance(time, distance):
    distance = 0.5 * 9.8 * time**2
    return distance


if __name__ == "__main__":
    main()

