import matplotlib.pyplot as plt
import numpy as np

# fill - закрашенный многоугольник.

x = [1, 3, 4, 5, 7]
y = [2, 4, 3, 4, 2]

fig, ax = plt.subplots(3, 1, figsize=(16, 16))

ax[0].plot(x, y)

ax[1].fill(x, y)

# fill может отображать несколько наборов данных.
t = np.linspace(0, 2 * np.pi, 100)
z = np.sin(t)
a = np.cos(t)
b = np.cos(t) / 2
c = np.cos(t) / 4
ax[2].fill(z, a, z + 2, b, z + 4, c)

ax[0].set(facecolor='seashell')
ax[1].set(title='Закрашенный график', facecolor='seashell')
fig.set(facecolor='floralwhite', figwidth=12, figheight=12)

plt.show()
