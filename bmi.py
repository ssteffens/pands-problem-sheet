# This program reads in a height and weight and calculates the BMI
# Author: Stefanie Steffens


# The input function returns a string so to be able to carry out the calculation, the values need to be converted to integer. 
height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))


# Height is entered in centimeters but needs to be converted to meters for the BMI calculation.
bmi = (weight/((height/100) ** 2))


# Output result has been rounded to 2 decimals for better readability.
print ('Your BMI is: {:.2f}' .format(bmi))