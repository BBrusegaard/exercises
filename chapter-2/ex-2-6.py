# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats

# Constants for the state and county tax rates


# Get the amount of purchase from the user, casting it to a float.
amount = float(input('What is the cost of your item?'))

# Calculate the state sales tax.
state_sales_tax = 6.12/100

# Calculate the county sales tax.
county_sales_tax = 7/100

# Sum the total tax.
total_tax = county_sales_tax + state_sales_tax

# Calculate the total of the sale.
total = total_tax*amount + amount

# Print detailed information about the sale, formatting all values to two decimal places.
print('The total cost of this sale is' , format(total, ".2f"))




