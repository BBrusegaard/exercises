# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.

# Global constants for fat calories per gram and carb calories per gram

# define the main function

    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    
    # Get grams of fat from the user.

    # Get grams of carbs from the user.

    # Calculate calories from fat.

    # Calculate calories from carbs.

    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments

# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

	# print each piece of information with floats formatted to 2 decimal places.

# Call the main function to start the program

FAT_CALORIES_PER_GRAM = 9.0
CARB_CALORIES_PER_GRAM = 4.0

def main():
    grams_of_fat = 0.0
    grams_of_carbs = 0.0
    grams_of_fat = float(input("Enter grams of fat amount: "))
    grams_of_carbs = float(input("Enter grams of carbs amount: "))
    calories_from_fat = FAT_CALORIES_PER_GRAM * grams_of_fat
    calories_from_carbs = CARB_CALORIES_PER_GRAM * grams_of_carbs
    calorie_detail(grams_of_fat, grams_of_carbs, calories_from_fat, calories_from_carbs)
    
def calorie_detail(grams_of_fat, grams_of_carbs, calories_from_fat, calories_from_carbs):
    print("Grams of fat:", format(grams_of_fat,".2f"))
    print("Grams of carbs:", format(grams_of_carbs,".2f"))
    print("Calories from fat:", format(calories_from_fat,".2f"))
    print("Calories from carbs:", format(calories_from_carbs,",.2f"))
    
main()