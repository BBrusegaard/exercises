def main():
    valid_number = False
    while not valid_number:
        user_input = ''
        user_input = input("Please enter a number:")
        try:
            int(user_input)
            valid_number = True
        except ValueError:
            print(user_input, 'is not a valid number!')
        else:
            valid_number = True
        
    print('Thank you, your number is', user_input)
main()