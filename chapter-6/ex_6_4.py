# Programming Exercise 6-4
#
# Program to count the number of lines in a text file.
# This program takes no user input, but requires the presence of a names.txt file,
# it opens this file and counts the lines, then closes it,
# and displays the count of lines.

# define the main function

    # Declare variables for line (string) and counter (int)

    # Open names.txt file for reading

    # Read the first line of the file to set up the while loop

    # While line is not empty, process the loop

        # increment the counter

        # read the next line

    # Close the file

    # Display the number of lines in the file

# Call the main function to start the program.

def main():
    line = ''
    counter = 0
    file_name = open('names.txt','r')
    line = file_name.readline()
    for x in line:
        counter += 1
        file_name.readline()
    file_name.close()
    print('The number of lines is',counter)
    
main()