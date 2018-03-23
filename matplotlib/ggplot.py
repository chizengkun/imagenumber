import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
r = 10
theta = np.linspace(0, 2 * np.pi, num=200)
x = r * (np.cos(theta) + theta * np.sin(theta))
y = r * (np.sin(theta) - theta * np.cos(theta))
n = 3
for i in range(n):
    angle = theta + 2 * np.pi * i / n
    x_new = x * np.cos(angle) - y * np.sin(angle)
    y_new = x * np.sin(angle) + y * np.cos(angle)
    plt.plot(x_new, y_new, '^')
plt.axis('equal')
plt.title('involute')
plt.show()