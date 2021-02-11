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

# Ask for input of float hours, float salary
input_hours = int(input('Enter the hours: '))
input_minutes = int(input('Enter the minutes: '))
print()

def add_time(hours,minutes):
    try:
        time_now = datetime.time(hours,minutes,00)

        new_time = time_now.hour , (time_now.minute+1)

        parsed_hours = new_time[0]
        parsed_minutes = new_time[1]

        if parsed_minutes == 60:
            parsed_minutes = 0
            parsed_hours += 1

        print('The entered time is: ',time_now)
        print("In one minute, it will be ",parsed_hours,"hour(s) and ",parsed_minutes, " minutes")
        print (line)
        print()
        
    except:
        print('please enter a valid time. Ex: 12 02')
        print (line)
        print()

add_time(input_hours,input_minutes)