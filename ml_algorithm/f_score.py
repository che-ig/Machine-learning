import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(
    nrows=1, ncols=3, layout="constrained", subplot_kw={"projection": "3d"}
)
_x = np.linspace(0, 1, 50)
_y = np.linspace(0, 1, 50)
x, y = np.meshgrid(_x, _y)
betta = [1, 2, 0.5]

for i, v in enumerate(betta):
    f = (1 + v**2) * (x * y) / (x * v**2 + y)
    ax[i].plot_surface(x, y, f, cmap="coolwarm", alpha=0.5)
    ax[i].view_init(elev=10, azim=-135)
    ax[i].set(title=f"betta is {v}", xlabel="precision", ylabel="recall")
plt.show()
