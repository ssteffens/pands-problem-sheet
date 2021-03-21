# This program displays a plot of the functions f(x) = x, g(x) = x**2, and h(x) = x**3 in the range [0,4].
# Author: Stefanie Steffens

# superscript found here: https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python
# xticks found here: https://stackoverflow.com/questions/17574420/how-can-i-set-x-axis-tick-marks-with-only-whole-numbers

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(5))            #range() function start from 0 and stops before the specified number (5)
ypointsF = xpoints
ypointsG = xpoints * xpoints
ypointsH = ypointsG * xpoints

plt.plot(xpoints, ypointsF, label = "f(x) = x", color = "red", marker = "o")
plt.plot(xpoints, ypointsG, label = "g(x) = x\u00b2", color = "blue", marker = "o")
plt.plot(xpoints, ypointsH, label = "h(x) = x\u00b3", color = "green", marker = "o")
plt.xticks(xpoints)
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend()
plt.show()