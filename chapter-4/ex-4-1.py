# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program will prompt the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers

# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day

	# input bugs collected on this day and convert it to an int

    # add bugs collected to total bugs

# Display the total number of bugs collected for all five days.

bugs_collected = 0 
total = 100

for i in range(5):
    bugs_collected += (int(input('Please enter the number of bugs collected today:')))
    
total = total + bugs_collected
print('The total bugs collected in five days is:' , total)

