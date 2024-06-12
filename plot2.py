import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.arange(-3, 3, 0.1)
y = np.arange(-2, 2, 0.1)

x, y = np.meshgrid(x, y)

z1 = np.exp(-(x**2 + y**2))
z2 = np.exp(-((x - 1)**2 + (y - 1)**2))

z = (z1 - z2)**2

ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot')

plt.show()