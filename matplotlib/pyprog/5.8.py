import matplotlib.pyplot as plt
import numpy as np

# Contour - линии уровней.
x, y = np.mgrid[-3 * np.pi:3 * np.pi:100j, -3 * np.pi:3 * np.pi:100j]
z = np.sinc(x) + np.cos(y)
fig, ax = plt.subplots()
ax.contour(z, levels=20)

fig.set(figwidth=8, figheight=8)

plt.show()
