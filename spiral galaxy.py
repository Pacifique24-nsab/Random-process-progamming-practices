import numpy as np
import matplotlib.pyplot as plt

# Define the number of points in the spiral and the number of spirals
num_points, num_spirals = 1000, 2

# Create the theta and r arrays
theta = np.linspace(0, 4*np.pi*num_spirals, num_points)
r = theta**2

# Convert to cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y, '.', color='white')

# Set the title and labels
plt.title('Spiral Galaxy')
plt.xlabel('x')
plt.ylabel('y')

# Set the background color to black
plt.gca().set_facecolor('black')

# Show the plot
plt.show()
