# 6. Write a script named product_sign.py
# hat asks the user for two numbers and then
# inform whether their product is negative or
# positive.

# Documentation: https://en.wikipedia.org/wiki/Truth_table

# Variables
line = '------------------------------------------'
title = '|            SIGN CALCULATOR             |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int x, int y -> x*y
x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))
print()

# TRUTH TABLE
# 1 = pos & 0 = neg
#-------------------
# 1   |   1   = pos
# 1   |   0   = neg
# 0   |   1   = neg
# 0   |   0   = pos

# Exclusive NOR logical equality

# product_sign function that integrate the xnor logical equality and if prod = 0 -> print 0
def product_sign(v_x, v_y): 
    if (v_x > 0) and (v_y > 0): product_sign = "+"
    elif (v_x > 0) and (v_y < 0): product_sign = "-"
    elif (v_x < 0) and (v_y > 0): product_sign = "-"
    elif (v_x < 0) and (v_y < 0): product_sign = "+"
    else : product_sign = "0"
    print('The product\'s sign is: ', product_sign)
    print (line)
    print()

# Execute function with provided parameters
product_sign(x,y)