# This program outputs whether or not today is a weekday. 
# Author: Stefanie Steffens


# First step: Import the datetime module to determine the current day of the week. 
# The "weekdays" list stores the names of the weekdays and will be used to establish whether today is a weekday or not. 

import datetime                                                     # imports datetime module
today = datetime.datetime.now().strftime("%A")                      # datetime.datetime.now() extracts current date and time
                                                                    # strftime("%A") displays the weekday (full version, i.e., Monday) from current date and time
                                                                    # reference used: https://www.w3schools.com/python/python_datetime.asp
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] # list of weekdays


# Second step: Output which day of the week is today, and whether it is a weekday or weekend using the print() function. 

print ("Today is {}. ".format(today))                               # prints what day is today

if today in weekDays:                                               # checks if today is contained in the list of weekdays
    print("Yes, unfortunately today is a weekday. :-(")                 # if yes, prints out that it is a weekday 
else:                                                                   # if no, prints that it is the weekend
    print("It is the weekend, yay! :-)")