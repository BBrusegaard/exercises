# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function

    # Define local variables to hold two integers

    # prompt the user for the first integer
    
    # prompt the user for the second integer

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments

 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.

	# if the first integer is greater, return the first integer
	# else, return the second integer


# Call the main function to start the program
def main():
    first_integer = 0
    second_integer = 0
    first_integer = int(input("Please enter an integer:"))
    second_integer = int(input("Please enter an integer:"))
    greater = compare_integers(first_integer, second_integer)
    print(greater)
    
    
def compare_integers(first, second):
    if first > second:
        print(first, "is greater")
        return first
    else:
        print(second, "is greater")
        return second
    
main()