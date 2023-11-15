import matplotlib.pyplot as plt
import numpy as np

plt.title("Task number 13")
x = np.array(["Car", "Public transport", "Bike", "foot"])
y = np.array([25, 19, 32, 7])

plt.bar(x, y)
plt.show()