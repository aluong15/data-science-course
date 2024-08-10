# 1. **Line Plot**: Create a Matplotlib line plot for a sine wave.

import matplotlib.pyplot as plt
import numpy as np

# angles in deg
# t = [-180, -150, -135, -120, -90, -60, -45, -30, 0, 30, 45, 60, 90, 120, 135, 150, 180]

# plot evenly spaced values
t = np.linspace(-np.pi,np.pi)

# convert to radians
# x = [i * (np.pi/180) for i in t]

plt.plot(t, np.sin(t), marker=".")
plt.title("sine wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()
