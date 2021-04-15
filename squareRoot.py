# This program reads in a positive floating-point number and outputs an approximation of its square root.
# Author: Stefanie Steffens


# Approach: 
    # The program uses the Newton Method for estimating squareroots 
    # Reference used: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root


# Consideration 1: 
    # Need to determine a square number that is close to the number provided as input. Its square root serves as the starting point (x0) for the estimation.
    # For example, if input number is 14.4, the nearest square numbers are 9 and 16, x0 can therefore be 3 or 4. 
    # This program uses the nearest square number smaller than the number provided through input. 

    # The first part of the sqrt() function identifies this square number and its root.
    # This is achieved by calculating the square number for each integer starting from 0 up to the number entered. 
    # Once the square number is larger than the number entered, the function stops and adds all square roots identified so far into a list (rootslist). 
    # The last (root) number added the the rootslist is used as x0. 

    # Note that this method only works for numbers equal to or larger than 1. If the entered number was smaller than 1, the rootslist would get populated with 0, resulting in x0 = 0.
    # The calculation in the second part of the program would then return an invalid result with divisor 2*x0 = 0. To prevent this scenario, the x0 value for numbers <1 is set to 1 by default.


# Consideration 2: 
    # The second part of the function carries out the calculation as per Newton's method. 
        # xnew = xprev - (f(xprev)/f'(xprev)) = xprev - ((xprev ** 2 - number)/(2*xprev))
        # Example for calculating x1: 
            # x1 = x0 - (f(x0)/f'(x0)) = x0 - ((x0**2 - a)/(2*x0)
            # The result of x1 is then re-entered into the formula (replacing x0) to calculate x2, etc.
        # This program uses 5 iterations of the calculation loop. 


# First step: Capture a positive float number using the input() function.
# The input() function returns a string so to be able to carry out the calculations, the value needs to be converted to float.

number = float(input("Please enter a positive number: "))

# The rootslist serves as a "collection pool" of integer values.
rootslist = []


# Second step: Define a function sqrt() which identifies x0 and then carries out the square root estimation.  

def sqrt():
# Part 1 of the function identifies the integer number to be used as the first estimate x0. 

    if number < 1:                                              # If the float number is less than 1, 
        rootslist.append(1)                                         # 1 is added to the rootslist to be used as the first estimate
    else:                                                       # If the float number is 1 or higher,
        for i in range(0,round(number+1)):                          # for every integer i between 0 and the inputted number (the root cannot be bigger than the square number):
            square = i*i                                                # calculate the square number of i
            if square > number:                                         # and compare the result to the inputted number. Once the square is bigger than the number entered, 
                break                                                   # the function stops.
            rootslist.append(i)                                         # All numbers i up to this point are added to the rootslist

    x0 = rootslist[-1]                                          # The last entry to the rootslist (indicated by -1) is set as x0 for the calculation.  


# Part 2 of the function carries out the calculation approximating the square root. 
# Number of iterations: 5

    xprev = x0                                                  # Sets xprev to the value of x0 so that it can be used in the below calculation. 
                                                                # Note that this step is only added to document the thought process, from a programming perspective it would be sufficient to set xprev to the last entry of the rootslist.
    count = 1                                                   # Sets the iteration counter to 1

    while count < 6:                                            # While the iteration counter is less than 6, 
        xnew = xprev - ((xprev ** 2 - number)/(2*xprev))            # calculates the square root estimation
        xprev = xnew                                                # "Re-sets" xprev to the value retrieved through estimation calculation
        count += 1                                                  # Increases counter by one
        if number%xprev == 0:                                   # In case the number entered already is a square number (e.g. 16), x0/xprev equals the number entered (i.e., if divided by two, remainder is 0),
            break                                                   # the function stops st this stage because no further calculation is required. 
    return xnew


# Third step: Call function sqrt().
# Output the identified square root using the print() function. 
# For better readability, the output result has been rounded to 2 decimals.

squarer = sqrt()
print("The square root of {} is approx. {:.2f}".format(number, squarer))