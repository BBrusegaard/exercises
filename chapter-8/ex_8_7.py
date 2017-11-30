# Programming Exercise 8-7
#
# Program to count upper and lower case letters, spaces and digits in a text file.
# This program accepts no input,
# opens hard-coded file, checks each character for upper, lower, digit or space,
# and displays the total of each on the screen.



# define the main function

    # define a constant for file to check (text.txt)

    # define local int variables for upper, lower, space and digit totals

    # define a local string variable to hold file contents

    # place file operations in a try block

        # Open file to check for reading.

        # Read in file contents from the file.

        # Step through each character in the file.

            # if the character is lower case, increment lower total,

            # else if the character is space, increment space total,

            # else if the character is upper case, increment  upper total,

            # else if the character is a digit, increment digit total
            
        
        # Close the file.
            
        # Display the totals.

    # use an except block to catch any IOError

        # print a file error message

    # Use a generic except block to catch all other exceptions.

        # print a generic error message



# Call the main function to start the program


