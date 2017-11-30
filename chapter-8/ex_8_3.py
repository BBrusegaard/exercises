# Programming Exercise 8-3
#
# Program to convert a short date to long format date.
# This program prompts a user for a short date (01/01/2020),
# splits it into a list of parts and chooses a month name based on its number,
# then displays the date in the longer form with the month name.

# Define the main function.

    
    # Define local int variables for day, month and year
    # and string variables for month name, date input and long date


    # Define a month list including January through December

    
    # Get the date input in mm/dd/yyyy from the user.


    # Split date input into date parts on the / character


    # the code will have to cast inputs to ints, so use a try block

        # Obtain month, day and year numbers from the date parts

        # Get the month name from the month list


        # Create string for long date using the month name

        # Display long date

    
    # use an except block to catch any ValueError caused by casting invalid input

        # display a message to indicate the user input was incorrect

    # use a generic except block for any other exceptions

        # display generic error message



# Call the main function to start the program


