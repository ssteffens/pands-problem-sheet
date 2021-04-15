# This program reads in a text file specified in the command line and outputs the number of "e"s it contains. 
# Author: Stefanie Steffens

# The program is based on the asumption that the request is to output the number of both lower and upper case "e"s contained in the file.

# The program was written based on these instructions how to access text file content using the command line: https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python


# First step: Import sys module to allow use of the argv function. 

import sys


# Second step: Define a function which reads the content of a text file that is provided in the command line.

def read_file():
    with open (sys.argv[1], "rt") as f:                     # open the text file indicated in the command line
        return f.read()                                     # returns content of the file


# Third step: Call the read_file() function and count all "e"s and "E"s contained in the file using the count() method. 
# References used: 
    # For using the count() method: https://www.w3schools.com/python/ref_string_count.asp
    # For using the count() method to count instances of more than one value: https://stackoverflow.com/questions/32414205/count-multiple-letters-in-string-python
# Output the count using the print() function. 

contents = read_file()                                      # stores the content of the file accessed in read_file() function in a variable called "contents"
countE = contents.count("e") + contents.count("E")          # counts and adds all "e"s and "E"s in "contents"

print(countE)                                               # prints out the count