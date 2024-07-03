import numpy as np

import matplotlib.colors as mcolors
from matplotlib import pyplot as plt

bc = mcolors.BASE_COLORS

x = np.linspace(0, 30, 30).round()
y = np.random.randint(2, 10, size=len(x))
y2 = np.arange(30)
plt.figure(figsize=(12, 7))
plt.plot(x, y, "s-.r", alpha=0.7, label="first")  # , mec='g'
plt.plot(x, y2, "s-.m", label="second", markevery=3)
plt.fill_between(x, y2, y2 + 3, color="c", alpha=0.3, where=(y2 <= 20))
plt.fill_between(x, y2, y2 - 2, color="r", alpha=0.3, where=(y2 >= 20))
plt.legend()
plt.xlim(0)
plt.ylim(0)
plt.grid()

plt.show()
