# This program reads in a weight and height and calculates the BMI
# Author: Stefanie Steffens

weight = int(input('Enter your weight in kg: '))
height = int(input('Enter your height in cm: '))

# Height is entered in centimeters but needs to be converted to meters for the BMI calculation
bmi = (weight/((height/100) ** 2))

# Output result has been rounded to 2 decimals for better readability
print ('Your BMI is: {:.2f}' .format(bmi))