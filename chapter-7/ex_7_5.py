# Programming Exercise 7-5
#
# Program to check to see if a user-supplied account number is in a reference file.
# This program prompts the user for an account number,
# compares it to the values stored in a text file,
# and displays a message indicated whether it was found.



# define the main function

    # define a string constant to hold the reference list file name (charge_accounts.txt)

    # define a local string variable to hold an account number to check



    # use a try block whenever accessing stored data


        # Open the reference list file for reading

        # Read all the lines in the file into an account list

        # use a loop to strip trailing '\n' from all account list elements        for i in range(len(accounts)):

        # prompt the user for an account number to check

        # if  account number to check is in account list

            # display a success message

        # else

            # display a failure message

    # use an except block to catch IOError

        # display a message indicating the file could not be opened

    # use a generic except block for any other errors



# Call the main function to start the program


