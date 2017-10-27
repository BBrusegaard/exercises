# Programming Exercise 6-2
#
# Program to read up to five lines of a file and display them.
# This program prompts the user for a file name,
# attempts to open and read five lines of the file,
# then displays those lines and finally closes the file.

# define a main function

    # Declare local variables, line and filename as strings and counter as int
    
    # Prompt the user for a file name

    # Open the specified file for reading

    # Read the first line of the file and increment the line counter to 1
    # this is needed to prepare conditions for the while loop to follow

    # Use a while loop to read until counter is 5 or reading produces no data

	# remove carriage returns before display, as print() supplies its own

        # print the current line

        # read the next line

        # Update counter when line is read

    # Close file

# Call the main function to begin the program

def main():
    line = ''
    file_name = ''
    counter = 0
    file_name = str(input("Enter file name: "))
    file_name = open(file_name,'r')
    line = file_name.read(1)
    while line <= 5:
        print(file_name.rstrip())
        line = line.read()
        return line
    file_name.close

main()