#prompt the user to enter a number
#between some MIN and MAX value

#If the number is between those values
#thank them, otherwise tell them it is not 
#within range or not a valid number

def main():
    number_in_range = False
    while not number_in_range:
        user_input = '  '
        user_input = input("Please enter a number between 1 and 100: ")
        try:
            int(user_input)
            number_in_range = True
        except ValueError:
            print(user_input,'is not in range!')
        else:
            number_in_range = True
        print('Your number is in range.')
        
main()