import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-5, 5, 100)

# Define the equations of the lines
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

# Plot the lines
plt.plot(x, y1, color='blue', linestyle='-', label='$y = 2x + 1$')
plt.plot(x, y2, color='red', linestyle='--', label='$y = 2x + 2$')
plt.plot(x, y3, color='green', linestyle='-.', label='$y = 2x + 3$')

# Add title and labels
plt.title('Lines $y = 2x + 1$, $y = 2x + 2$, $y = 2x + 3$')
plt.xlabel('x')
plt.ylabel('y')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
