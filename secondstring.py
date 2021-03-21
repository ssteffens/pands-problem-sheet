# This program reads in a string and outputs every second letter in reverse order. 
# Author: Stefanie Steffens

# Program was written base on these instructions: https://www.w3schools.com/python/python_howto_reverse_string.asp 
# [::-2] [start:end:step] The slice statement removes every 2nd character, starting from the end (indicated by -)
# No start entered so it's considered position 0
# 0 entered as end of statement, reflecting the last letter of the sentence (which is not included in slicing)

sentence = input('Please enter a sentence: ')
print(sentence[:0:-2])