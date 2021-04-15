# This program reads in a string and outputs every second letter in reverse order. 
# Author: Stefanie Steffens


# The program was written based on these instructions: https://www.w3schools.com/python/python_howto_reverse_string.asp 


# First step: Capture the string using the input() function.

sentence = input("Please enter a sentence: ")


# Second step: Output every second letter of the string in reverse order using the print() function and slice syntax [start:end:step]. 
    # Start:  No start value entered so that the output starts at position 0. Due to reverse order, this reflects the end of the string entered. 
    # End:    No end value entered so that the output ends at the last character of the string. Due to reverse order, this reflects the beginning of the string entered. 
    # Step:   2 indicates that every second letter is returned, the - (minus) indicates reverse order starting at the end of the string. 

print(sentence[::-2])