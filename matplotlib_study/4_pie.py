import numpy as np
from matplotlib import pyplot as plt

vals = [24, 17, 53, 21, 35]
labels = ['Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar']
fig, ax = plt.subplots(1, 2, figsize=(9, 9))
ax[0].pie(vals, labels=labels, autopct='%1.1f%%', radius=1.5, explode=(0.1, 0, 0.15, 0, 0))
ax[0].axis('equal')

data = np.array([[5, 10, 7], [8, 15, 5], [11, 9, 7]])
offset=0.4
cmap = plt.get_cmap('tab20b')
b_colors = cmap(np.array([0, 8, 12]))
sm_colors = cmap(np.array([1, 2, 3, 9, 10, 11, 13, 14, 15]))
ax[1].pie(data.sum(axis=1), radius=1, colors=b_colors,
wedgeprops=dict(width=offset, edgecolor='w'))
ax[1].pie(data.flatten(), radius=1-offset, colors=sm_colors,
wedgeprops=dict(width=offset, edgecolor='w'))

plt.show()