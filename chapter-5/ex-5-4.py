# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.

# define the main function

    # Define local float variables for loan, insurance, gas, oil, tires and maintenance

    # Get the amount of the monthly loan payment from the user.

    # Get the amount of the monthly insurance from the user.

    # Get the amount of the monthly gas from the user.

    # Get the amount of the monthly oil from the user.

    # Get the amount for monthly tire wear from the users.

    # Get the amount for monthly maintenance from the user.

    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.

# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.

    # Define local float variables for monthly total and annual total

    # calculate the monthly total
    
    # calculate the annual total

    # Print monthly and annual information, formatting float value to 2 decimal places.

# Call the main function to start the program

def main():
    monthly_loan = 0.0
    monthly_insurance = 0.0
    monthly_gas = 0.0
    monthly_oil = 0.0
    monthly_tire_wear = 0.0
    monthly_maintenance = 0.0
    
    monthly_loan = float(input("Enter cost of montly loan amount: $"))
    monthly_insurance = float(input("Enter cost of monthly insurance amount: $"))
    monthly_gas = float(input("Enter cost of monthly gas amount: $"))
    monthly_oil = float(input("Enter cost of monthly oil amount: $"))
    monthly_tire_wear = float(input("Enter cost of monthly tire wear: $"))
    monthly_maintenance = float(input("Enter cost of monthly car maintenance: $"))
    
    car_expenses(monthly_loan, monthly_insurance, monthly_gas, 
    monthly_oil, monthly_tire_wear, monthly_maintenance)
    
def car_expenses(monthly_loan, monthly_insurance, monthly_gas, 
    monthly_oil, monthly_tire_wear, monthly_maintenance):
    monthly_total = 0.0
    monthly_total = (monthly_loan + monthly_insurance + monthly_gas + 
    monthly_oil + monthly_tire_wear + monthly_maintenance)
    year_total = monthly_total * 12
    print("The monthly total is: $", format(monthly_total, ".2f"))
    print("The average predicted annual total is: $", format(year_total, ".2f"))
        
main()