# Programming Exercise 5-5
#
# Program to compute assessed value and property tax.
# This program accepts a property value from a user,
# uses global constants to calculate an assessed value and property tax,
# then passes them to a function to display the results for the user.

# Global constants for assessment percentage and property tax rate

# define the main function

    # Define local float variables for property value, assessed value and property tax

    # Get the property value from the user.

    # Calculate the assessed value using the global constant

    # Calculate the property tax using the global constant

    # Call the function to display property tax information, 
    # passing assessed value and property tax as arguments

# Define a function to display property tax information.
# This function accepts the assessed value and property tax as parameters,
# performs no calculations,
# but displays the information with float variables formatted to 2 decimal places.

	# display the assessed value
	
	# display the property tax

# Call the main function to begin the program.

ASSESSMENT_PERCENTAGE = 0.8
PROPERTY_TAX_RATE = 0.114

def main():
    property_value = 0.0
    assessed_value = 0.0
    property_tax = 0.0
    property_value = float(input("Enter your property value: $ "))
    assessed_value = ASSESSMENT_PERCENTAGE * property_value
    property_tax = PROPERTY_TAX_RATE * property_value
    tax_information(assessed_value, property_tax)
    
def tax_information(assessed_value, property_tax):
    print("Your assessed property value is: $" ,format(assessed_value, ".2f"))
    print("Your property tax is: $" ,format(property_tax, ".2f"))
    
main()