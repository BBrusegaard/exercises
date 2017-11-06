#Main
    #Prompt
    #Choose
    #Display

# This program allows the user to choose various geomtery calculations from a menu. 
# This program imports the circle and rectangle modules.
import circle
import rectangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()
        
        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        output = handle_choice(choice)
        print(output)
            
    # The display_menu function displays a menu.
def display_menu():
    print(' MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
        
def handle_area_of_circle():
    radius = float(input("Enter the circle's radius: "))
    return "The area is " + str(circle.area(radius))

def handle_circumference_of_circle():
    radius = float(input("Enter the circle's radius: "))
    return "The circumference is" + str(circle.circumference(radius)) 
    
def handle_area_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The area is" + str(rectangle.area(width, length))
    
def handle_perimeter_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The perimeter is" + str(rectangle.perimeter(width, length))
        
def handle_choice(choice):
    # Perform the selected action.
    if choice == AREA_CIRCLE_CHOICE:
        return handle_area_of_circle()
    elif choice == CIRCUMFERENCE_CHOICE:
        return handle_circumference_of_circle()
    elif choice == AREA_RECTANGLE_CHOICE:
        return handle_area_of_rectangle()
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        return handle_perimeter_of_rectangle()
    elif choice == QUIT_CHOICE:
        print('Exiting the program...')
    else:
        print('Error: invalid selection.')
            
    # Call the main function.
main()