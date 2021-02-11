# 5. Write a script named grades.py that
# convert any grade N, entered by the user in
# the form of points (for example 27 out of 85),
# into a standardized grade according to the
# following table:

# Grade             |   Standardized Grade
#-------------------------------------
# N >= 80%          |   A
# 80 % > N >= 60 %  |   B
# 60 % > N >= 50 %  |   C
# 50 % > N >= 40 %  |   D
# N < 40 %          |   E

# Variables
line = '------------------------------------------'
title = '|           GRADE CALCULATOR             |'

# Header
print (line)
print (title)
print (line)

# Ask for input of float result, float ponderation
grade = float(input('Enter student\'s grade: '))
ponderation = float(input('Enter the ponderation: '))
print()

# Calculate letter grade of the student 
def letter_grade(score): 
    if score >= 80: letter_grade = "A"
    elif score >= 60: letter_grade = "B"
    elif score >= 50: letter_grade = "C"
    elif score >= 40: letter_grade = "D"
    else : letter_grade = "E"
    print('The student\'s grade is: ', letter_grade)
    print (line)
    print()

# Display results
formated_grade = grade*100/ponderation
letter_grade(formated_grade)