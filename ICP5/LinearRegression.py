# import the required library numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt


# Given the features X and Y
x = np.array([2.9, 6.7, 4.9, 7.9, 9.8, 6.9, 6.1, 6.2, 6, 5.1, 4.7, 4.4, 5.8])
y = np.array([4, 7.4, 5, 7.2, 7.9, 6.1, 6, 5.8, 5.2, 4.2, 4, 4.4, 5.2])

# calculate the mean of X
xMean = np.mean(x)

# calculate the mean of y
yMean = np.mean(y)

# to calculate the coefficient of equation y = mx + c where B1 is the slope
B1 = (np.sum((x-xMean)*(y-yMean)))/(np.sum(np.power((x-xMean), 2)))

# calculate the y intercept of the linear equation y=mx+c where c is intercept of y
B0 = yMean-(B1*xMean)

# plot the x and y values
plt.scatter(x, y)

# linear regression equation with b1 as slope and b0 as y intercept

ry = B1*x+B0

# plot the line that best separates the data points

plt.plot(x, ry)

# show the plot for the linear regression model

plt.show()
