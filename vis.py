import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# File path
file_path = 'colmap_text/points3D.txt'

# Initialize lists to store data
points = []
colors = []

# Read data from file
with open(file_path, 'r') as f:
    for line in f:
        if line.startswith('#') or line.strip() == '':
            continue
        data = line.strip().split()
        # Extracting point coordinates (X, Y, Z)
        x = float(data[1])
        y = float(data[2])
        z = float(data[3])
        points.append((x, y, z))

        # Extracting color (R, G, B)
        r = int(data[4])
        g = int(data[5])
        b = int(data[6])
        colors.append((r / 255, g / 255, b / 255))  # Normalize to [0, 1]

# Convert lists to numpy arrays for plotting
points = np.array(points)
colors = np.array(colors)

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, marker='o')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Point Cloud Visualization')

# Show plot
plt.show()
