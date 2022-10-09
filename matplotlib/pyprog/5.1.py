import matplotlib.pyplot as plt
import numpy as np

# Цвет линии

x = np.zeros(8)
fig, ax = plt.subplots()

# RGB
ax.plot(x, color=(0.9, 0.2, 0.9))

# RGBA
ax.plot(np.arange(-1, 7), color=(0.9, 0.2, 0.9, 0.5), linewidth=12)

# hex RGB
ax.plot(x + 1, color='#0a0b0c')

# hex RGBA
ax.plot(x + 2, color='#0a0b0c3a')

# Уровень серого в интервале [0, 1]
ax.plot(x + 3, color='0.3')

fig.set(facecolor='mintcream', figwidth=12, figheight=6)
ax.set(facecolor='whitesmoke')

plt.show()
