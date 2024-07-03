import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
# fig, ax = plt.subplots(figsize=(4, 4))
# gr = ax.pcolor(vals) #  cmap=plt.get_cmap('viridis', 11)
# axins = inset_axes(ax, width='7%', height='30%', loc='lower left',
# bbox_to_anchor=(1.01, 0., 1, 1), bbox_transform=ax.transAxes, borderpad=0)
# plt.colorbar(gr, ticks=[0, 5, 10], cax=axins, label='Value')

plt.pcolor(vals, cmap=plt.get_cmap("viridis", 11))
plt.colorbar(orientation="horizontal", shrink=0.9, extend="max", label="Value")
plt.show()
