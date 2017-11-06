# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function

    # define local variables for average and five scores

    # Get five scores from the user

    # find the average by passing the scores to a function that returns the average

    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    
    # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average

# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.

    # define a local float variable to hold the average
    
    # calculate the average
    
    # return the average

# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.

    # if score is 90 or more, return A
    
    # 80 or more, return B
    
    # 70 or more, return C
    
    # 60 or more, return D
    
    # anything else, return F

# Call the main function to start the program

def main():
    average = 0
    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0
    score_5 = 0
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    F = 'F'
    score_1 = int(input("Enter first score (integer): "))
    score_2 = int(input("Enter second score (integer): "))
    score_3 = int(input("Enter third score (integer):  "))
    score_4 = int(input("Enter fourth score (integer): "))
    score_5 = int(input("Enter fifth score (integer): "))
    average = numeric_score(score_1,score_2,score_3,score_4,score_5)
    grade = letter_grade(A,B,C,D,F,average)
    print('5 Scores')
    print('--------------------')
    print(score_1)
    print(score_2)
    print(score_3)
    print(score_4)
    print(score_5)
    print('Average',' ','Letter Grade')
    print('--------------------')
    print(average,'     ',grade)
    letter_grade(A,B,C,D,F,average)
    numeric_score(score_1,score_2,score_3,score_4,score_5)
    
    
def numeric_score(score_1,score_2,score_3,score_4,score_5):
    average = int
    average = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
    return average
    

def letter_grade(A,B,C,D,F,average):
    if average >= 90:
        return A
    elif average < 90 and average >= 80:
        return B
    elif average < 80 and average >= 70:
        return C 
    elif average < 70 and average >= 60:
        return D 
    elif average < 60:
        return F
    return letter_grade(A,B,C,D,F,average)
        
        
main()