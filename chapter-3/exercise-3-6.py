# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string

# Get month and cast it to int
# Get day and cast it to int
# Get year and cast it to int

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
	# set message to hold "invalid month" message
# else if day input is out of range
    # set message to hold "invalid day" message
# else if  year input is out of range (greater than 99 or less than 0)
    # set message to hold "invalid year" message
# else 
    # set message to hold the date in 00/00/00 form
    
    # if day * month equals year, add " is a magic date" to message
    
    # else add " is not a magic date" to message

# print message for the user
print('A magic date is a date where the day multiplied by the month equals the year. Answer the following to find one.')
month = int(input('Please enter the numerical value for a month:'))
day = int(input('Please enter the numerical vaule for a day:'))
year = int(input('Please enter a year (last 2 digits):'))
magic = day * month == year

if 0 >= month or month >= 13:
    print('Invalid month!')
if 0 >= day or day >= 32:
    print('Invalid day!')
if 0 >= year or year > 99:
    print('Invalid year!')
else:
    print('The date is:', format(month,'02d'),'/', format(day,'02d'),'/', format(year,'2d'))
if magic == True:
    print(format(month,'02d'),'/', format(day,'02d'),'/', format(year, '2d') , 'Is a magic date.', )
elif magic == False:
    print(format(month,'02d'),'/', format(day,'02d'),'/', format(year, '2d') , 'Is not a magic date.')