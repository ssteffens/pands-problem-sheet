# This program reads in a text file and outputs the number of "e"s is contains. 
# Author: Stefanie Steffens

# The program is based on the asumption that the request is to output the number of both lower and upper case "e" contained in the file.
# How to access text file content using the command line
# https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python


import sys


def readFile():
    with open (sys.argv[1], "rt") as f: 
        return f.read()

contents = readFile()
countE = contents.count("e") + contents.count("E")           # https://www.w3schools.com/python/ref_string_count.asp
                                                            # https://stackoverflow.com/questions/32414205/count-multiple-letters-in-string-python
print(countE)