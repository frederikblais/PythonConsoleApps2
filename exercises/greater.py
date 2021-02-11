# 4. Write a script named greater.py, which will
# prompt the user 3 integer values and show
# the greater.

# Variables
line = '------------------------------------------'
title = '|         GREATER INT CALCULATOR         |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int x,y,z
x = int(input('Enter the integer value of x: '))
y = int(input('Enter the integer value of y: '))
z = int(input('Enter the integer value of z: '))
print()

# Greater function that compare and check the greater value between x,y,z
def greater (v_x,v_y,v_z):
    if(v_x > v_y) and (v_x > v_z):
        greater = v_x
    elif(v_y > v_x) and (v_y > v_z):
        greater = v_y
    else:
        greater = v_z

    # Print result
    print("The greater integer is: ", greater)
    print()
    print(line)

# Call the Greater function
greater (x,y,z)