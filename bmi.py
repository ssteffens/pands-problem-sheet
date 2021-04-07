# This program reads in a height and weight. Based on the provided information it calculates and outputs the BMI. 
# Author: Stefanie Steffens


# First step: Capture values for height and weight using the input() function. 
# The input() function returns a string so to be able to carry out the calculation, the values need to be converted to integer. 

height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))


# Second step: Calculate the BMI by dividing the provided weight by square of the provided height. 
# The height is entered in centimeters but needs to be converted to meters for the BMI calculation. This is achieved by dividing the height (in cm) by 100. 

bmi = (weight/((height/100) ** 2))


# Third step: Output the BMI result using the print() function. 
# The output result has been rounded to 2 decimals for better readability.

print('Your BMI is: {:.2f}' .format(bmi))