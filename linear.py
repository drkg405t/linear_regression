import numpy as np
import matplotlib.pyplot as plt

# define the number of coefficients necessary
number_of_points = 500
x_point = []
y_point = []
a = 0.5
b = 0.75

# iterate variables for generating 500 random points
for i in range(number_of_points):
    x = np.random.normal(0.0, 0.5)
    y = a * x + b + np.random.normal(0.0, 0.1)
    x_point.append([x])
    y_point.append([y])

# plot the points
plt.plot(x_point, y_point, 'o', label = 'Input Data')
plt.legend()
plt.show()
    
