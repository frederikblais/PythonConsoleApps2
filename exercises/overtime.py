# 7. Write a script named overtime.py that
# calculates the amount of overtime for an
# employee, knowing the unit price of an hour,
# according to the following scale:

# The first 39 hours without supplement
# From the 40 to 44, these hours are increased by 50%
# From the 45 to 49, these hours are increased by 75%
# From 50 hours or more, these hours are increased by 100%.

# Variables
line = '------------------------------------------'
title = '|          OVERTIME CALCULATOR           |'

# Header
print (line)
print (title)
print (line)

# Ask for input of float hours, float salary
hours = float(input('Enter the amount of hours done in the week: '))
salary = float(input('Enter the salary: '))
print()

def overtime_calc (s,h):
    if(h<=40):result = s * h
    elif(h<=45):result = (s*40)+((s*1.5)*(h-40))
    elif(h<=50):result = (s*40)+((s*1.75)*(h-40))
    else:result = (s*40)+((s*2)*(h-40))
    print('The employee\'s week salary is: $ {0:.2f}'.format(result))
    print (line)
    print()

# Print result
overtime_calc(salary,hours)