# 3. Make a script named leap year.py, which
# would display TRUE if the year entered by the
# user is a leap year and FALSE otherwise.

# Variables
line = '------------------------------------------'
title = '|          LEAP YEAR CALCULATOR          |'

# Header
print (line)
print (title)
print (line)

# Ask for input of a year
y = int(input('Enter the year you want to verify: '))
print()

# If y is / by 4
if y % 4 == 0:
    # If y is a multiple of 100
   if y % 100 == 0:
       # If y is a multiple of 400
       if y % 400 == 0:
           print('%0.0f is a leap year' % y)
           print (line)
       else:
           print('%0.0f is not a leap year' % y)
           print (line)
   else:
       print('%0.0f is a leap year' % y)
       print (line)
else:
       print('%0.0f is not a leap year' % y)
       print (line)