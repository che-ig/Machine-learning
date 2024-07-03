import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 100)
y = (x - 2) * (x + 2)

fig, ax = plt.subplots(1, 3, figsize=(16, 10))
ax[0].plot(x, y, color="g")
ax[0].grid(color="b", linestyle="--")

# Вертикальные линии.
ax[0].vlines(0, y.min(), y.max())
ax[0].vlines(-2, y.min(), y.max(), color="r")
ax[0].vlines(2, y.min(), y.max(), color="r")

# Горизонтальные линии.
ax[0].hlines(0, -5, 5)
ax[0].hlines(-4, -5, 5)

# В качестве данных могут выступать послодовательности.
z = np.arange(10)
x_min = np.linspace(-10, 0, 10)
x_max = np.linspace(1, -10, 10)
ax[1].hlines(z, x_min, x_max, color="b", linewidth=4, linestyle="--")

# Тоже самое можно делать и с vlines
ax[2].vlines(z, x_min, x_max, color="m", linewidth=5, linestyle=":")

plt.show()
