import numpy as np
import matplotlib.pyplot as plt

# Create numpy arrays for x and y values
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

# Plot the scattering pattern of the points
plt.scatter(x, y, marker='+', color='blue')

# Add title and labels
plt.title('Scatter Plot of Points $(x, y)$')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.grid(True)
plt.show()
