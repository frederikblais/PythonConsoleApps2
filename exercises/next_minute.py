# 8. Write a script named next_minute.py that
# will read the hour and minutes on the
# keyboard, and it will display what time it is
# one minute later.

# Variables
import datetime

line = '------------------------------------------'
title = '|         NEXT MINUTE CALCULATOR         |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int hours, int minutes
input_hours = int(input('Enter the hours: '))
input_minutes = int(input('Enter the minutes: '))
print()

def add_time(hours,minutes):
    try:
        # Convert input ot time object
        time_now = datetime.time(hours,minutes,00)

        # Add 1 minute to the input time
        new_time = time_now.hour , (time_now.minute+1)

        # Parse from tuple object to int
        parsed_hours = new_time[0]
        parsed_minutes = new_time[1]

        # Error hadling for 23:59
        if parsed_minutes == 60:
            parsed_minutes = 0
            parsed_hours += 1
        if parsed_hours == 24:
            parsed_hours = 0

        # Print results
        print('The entered time is: ',time_now)
        print("In one minute, it will be ",parsed_hours,"hour(s) and ",parsed_minutes, " minutes")
        print (line)
        print()

    except:
        print('please enter a valid time format.')
        print (line)
        print()

# Execute function with input parameters
add_time(input_hours,input_minutes)