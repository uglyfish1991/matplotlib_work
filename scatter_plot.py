import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

number_of_placements=np.array(list(range(1,11)))
responses_received = np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])

m, c = np.polyfit(number_of_placements, responses_received, 1)

plt.scatter(number_of_placements, responses_received)
#? equation of a sraight line is y = mx+c
#? m is the slope
#? x is the indepedent variable
#? c is what y equals when x = 0
plt.plot(number_of_placements, m*number_of_placements+c)
plt.title("Job Posting Junior Dev Role")
plt.xlabel("Number of Places Advertised")
plt.ylabel("Responses Received")
plt.show()