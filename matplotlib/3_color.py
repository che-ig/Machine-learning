import numpy as np
from matplotlib import pyplot as plt

np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals)
plt.colorbar()
plt.show()