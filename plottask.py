# This program prints out a plot of the functions f(x) = x, g(x) = x**2, and h(x) = x**3 in the range [0,4].
# Author: Stefanie Steffens


# First step: Import the numpy library to use its array() function and the matplotlib.pyplot module to create and output the plot. 

import numpy as np
import matplotlib.pyplot as plt


# Second step: Define the number range [0, 4] using the numpy array() function. 
# Define the functions to be displayed in the plot. 

xpoints = np.array(range(5))                            # range() function starts from 0 and stops before the specified number (5)
ypointsF = xpoints                                      # function f(x) = x
ypointsG = xpoints * xpoints                            # function g(x) = x**2
ypointsH = xpoints * xpoints * xpoints                  # function h(x) = x**3


# Third step: Plot the functions using matplotlib, using different colours and labels for easier differentiation.
# Configure the plot output by adding axis labels, a legend and xticks
# References used: 
    # For printing superscript: https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python
    # For adding x-axis ticks marks using whole number values: https://stackoverflow.com/questions/17574420/how-can-i-set-x-axis-tick-marks-with-only-whole-numbers

plt.plot(xpoints, ypointsF, label = "f(x) = x", color = "red", marker = "o")
plt.plot(xpoints, ypointsG, label = "g(x) = x\u00b2", color = "blue", marker = "o")
plt.plot(xpoints, ypointsH, label = "h(x) = x\u00b3", color = "green", marker = "o")

plt.xticks(xpoints)                                     # add tick marks on x-axis using the numbers specified in the xpoints range
plt.xlabel("x-Axis")                                    # add label for x-axis
plt.ylabel("y-Axis")                                    # add label for y-axis
plt.legend()                                            # add legend
plt.savefig("plottask.png")                             # save plot as plottask.png
plt.show()                                              # display plot
