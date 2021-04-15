# This program asks the user to input a positive integer and outputs the successive values of the following calculation:
#   At each step calculate the next value by taking the current value.
#   If the current value is even, divide it by two.
#   If the current value is odd, multiply it by three and add one.
#   The program ends if the current value is one. 
# Author: Stefanie Steffens


# First step: Capture a positive integer number using the input() function. 
# The input() function returns a string so to be able to carry out the calculations, the values need to be converted to integer. 
# The list called "numbers" is used to store the initial input value and the values calculated from it. 

number = int(input("Please enter a positive integer: "))
numbers = []


# Second step: Carry out the calculations as per the instructions and add the values to a list. 

numbers.append(number)                  # Adds the inputted number to the "numbers" list
while number != 1:                      # Specifies that loops runs until number is equal to 1
    if (number % 2) == 0:               # For even numbers (i.e., if divided by two, remainder is 0): 
        evenNumber = int(number/2)          # carries out division by 2
        numbers.append(evenNumber)          # and adds the new number to the list
        number = evenNumber                 # changes the condition variable to start loop again
    else:                               # For not even (= odd) numbers (i.e., if divided by two, remainder is not 0):
        oddNumber = (number*3) + 1          # carries out calculation (multiply by 3, then add 1)
        numbers.append(oddNumber)           # and adds the new odd number to the list
        number = oddNumber                  # changes the condition variable to start loop again


# Third step: Output the values stored in the "numbers" list using the print() function. 

print(*numbers, sep=" ")                # Prints the list of numbers without brackets and separated by space 
                                        # Solution found here: https://stackoverflow.com/questions/17757450/how-to-print-a-list-with-integers-without-the-brackets-commas-and-no-quotes