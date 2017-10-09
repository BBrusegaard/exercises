# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats

# Get length A from the user and convert it to a float
Length_A = float(input('What is the length of rectangle A?'))

# Get width A from the user and convert it to a float
Width_A = float(input('What is the width of rectangle A?'))

# Get length B from the user and convert it to a float
Length_B = float(input('What is the length of rectangle B?'))

# Get width B from the user and convert it to a float
Width_B = float(input('What is the width of rectangle B?'))

# Calculate area A
area_A = Length_A * Width_A

# Calculate area B
area_B = Length_B * Width_B

# Print each area, formatting the values to 2 decimal places

print('The area of rectangle A is' , format(area_A, ".2f"))
print('The area of rectangle B is' , format(area_B, ".2f"))

# if area A is greater, print "A is greater" message.

if area_A > area_B:
    print('A is greater')
elif area_B > area_A:
    print('B is greater')
else:
    print('A and B are equal')
    
# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

