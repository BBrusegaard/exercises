#This program is trying to calculate all possible premutations of the equation x * y + z
limit = 10

def check_numbers(x,y,z):
    a = (x * y) / z
    b = x * (y / z)
    a = round(a, 3)
    b = round(b, 3)
    if abs(a - b) >= .002:
        print("Different values")
        print("First: ",a)
        print("Second: ",b)

def print_numbers(x,y,z):
    print("Check:", z)