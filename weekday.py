# This program outputs whether or not today is a weekday. 
# Author: Stefanie Steffens

import datetime                                                     # imports datetime module
today = datetime.datetime.now().strftime("%A")                      # datetime.datetime.now() extracts current date and time
                                                                    # strftime("%A") displays the weekday (full version, i.e. Monday from current date and time)
                                                                    # https://www.w3schools.com/python/python_datetime.asp
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] # list of weekdays

print ("Today is {}. ".format(today))                               # prints what day is today

if today in weekDays:                                               # checks if today is contained in the list of
    print("Yes, unfortunately today is a weekday. :-(")             # weekdays, if yes, prints out that it's a weekday 
else:                                                               # if no, prints that it's the weekend
    print("It is the weekend, yay! :-)")
