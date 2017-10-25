# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed

# Global constants for the state and county tax rates

# define the main function
    # Define local float variables for purchase, state tax and county tax

    # Get the purchase amount from the user
    
    # Calculate the state tax using the global constant for state tax rate

    # Calculate the county tax using the global constant for county tax rate

    # Call the sale details function, passing the purchase, state tax and county tax

# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
    # Define local float variables for total tax and sale total

	# Calculate the total tax
	
	# Calculate the total sale

    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
# Call the main function to start the program.

STATE_TAX = 0.06
COUNTY_TAX = 0.06

def main():
    state_tax = 0.0
    county_tax = 0.0
    purchase = float(input('Enter a purchase amount:'))
    state_tax = purchase * STATE_TAX
    county_tax = purchase * COUNTY_TAX
    sales_details(purchase, state_tax, county_tax)
    
def sales_details(purchase, state_tax, county_tax):
    total_tax = 0.0
    sales_total = 0.0
    total_tax = state_tax + county_tax
    sales_total = total_tax + purchase
    print('Your sales total is:', format(sales_total, ".2f"))
    
main()