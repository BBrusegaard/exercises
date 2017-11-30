# Programming Exercise 8-6
#
# Program to compute the average number of words per line in a text file.
# This program takes no input, but requires the presence of a file, text.txt,
# which it loops through, accumulating words per sentence, calculates the average
# Then displays the average number of words per sentence on the screen.



# Define the main function.

    # Define local int variables for number of sentences and total words

    # Define a local float variable for average words

    # Define empty list variables for words and sentences


    # I/O operations should be placed into a 'try' block

        # Open file text.txt for reading.


        # Read file lines into the sentences list.

        
        # iterate over each sentence in the sentences list

            # split the sentence into the list of words


            # add the length of the words list to total words


        # Get the number of sentences from the length of the sentences list.

        # Calculate average words per sentence from total words and number of sentences


        # Display average words per sentence

        # Close the file.


    # use an except block to catch any IOError, which a missing file can cause.

        # print a message to let the user know a file error has occurred.

    # Use an except block without an error type to catch all other exceptions.

        # let the user know an error occurred.



# Call the main function to start the program.


