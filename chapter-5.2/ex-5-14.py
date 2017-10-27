# Programming Exercise 5-14
#
# Program to compute kinetic energy from mass and velocity.
# This program accepts values for mass and velocity from the user in kilograms and meters per second,
# passes them to a function that returns kinetic energy in joules calculated from those values,
# and displays the result.

# define the main function

    # define local float variables for mass, velocity and kinetic energy

    # Get mass from user

    # Get velocity from user

    # Get kinetic energy in joules from the kinetic energy function

    # Display kinetic energy in joules, formatted to 2 decimal places.

# Define a function to calculate kinetic energy in joules.
# The function accepts two parameters, mass in kilograms and velocity in meters/second,
# uses a formula to calculate the joules of kinetic energy,
# and returns the result

    # Define a local variable for joules of kinetic energy

	# calculate the kinetic energy using the parameters and the conversion formula    

	# return the result

# Call the main function to start the program

def main():
    mass = 0.0
    velocity = 0.0
    mass = float(input("Enter the mass (kg): "))
    velocity = float(input("Enter the velocity (m/s): "))
    print("The kinetic energy is",format(calculate_kinetic_energy(mass, velocity),".2f"),"Joules")
    
def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = 0.0
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy    
    
main()