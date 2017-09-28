# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
item1 = float(input('What is the price of your first item?'))
item2 = float(input('What is the price of your second item?'))
item3 = float(input('What is the price of your third item?'))
item4 = float(input('What is the price of your fourth item?'))
item5 = float(input('What is the price of the fifth item?'))

total = float(item1*0.06+item1 + item2*0.06+item2 + item3*0.06+item3 + item4*0.06+item4 + item5*0.06+item5)
# Constant for the sales tax rate.
SALES_TAX_RATE = 0.06 

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.

print('Your total price is' , format(total, ".2f"))

# Calculate the subtotal by adding up the item prices.


# Calculate the sales tax by multiplying the subtotal by the tax rate.


# Calculate the total by adding the subtotal and tax.


# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 





