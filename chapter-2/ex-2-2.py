# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values

# Get the amount of projected sales.
# be sure to convert the input to a float


# Calculate the projected profit using a 23% profit margin.


# Print the projected profit.
# be sure to format the output to two decimal places
sales_total = 0.0
profit = float(0)

sales_total = input("Enter projected sales amount:")		#Prompts user for sales total     					
sales_total = float(sales_total)
profit = sales_total*0.23 + sales_total			#Calculates user input by 23% sales margin then adds user input of raw sales

print('Your projected sales are:',format(profit , ".2f"))				#Prints the total profit to user

