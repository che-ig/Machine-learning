import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 25, 5)
x[1:] = x[1:] - 1

y = np.random.randint(2, 10, size=5)
y2 = np.random.randint(2, 10, size=5)
y3 = np.random.randint(2, 10, size=5)

plt.plot(x, y, "o-r", label="line 1")
plt.plot(x, y2, "o-.g", label="line 2")
plt.legend(loc="upper right", shadow=True, edgecolor="m")  # ,bbox_to_anchor=(0.5, 1)

# plt.show()

# GridSpec
fg = plt.figure(figsize=(10, 4), constrained_layout=True)
# gs = gridspec.GridSpec(nrows=1, ncols=2,figure=fg)
gs = fg.add_gridspec(nrows=2, ncols=2)
plt.figtext(0.5, 0, "figtext")  # Подпись под всеми крафиками
plt.suptitle("suptitle")  # Заголовок над всеми графиками

fig_ax_1 = fg.add_subplot(gs[0, 0])
plt.plot(x, y, "m--")

fig_ax_2 = fg.add_subplot(gs[0, 1])
plt.plot(x, y2, "b-.")

fig_ax_3 = fg.add_subplot(gs[1, :])
bbox_3 = dict(boxstyle="circle", facecolor="y", ec="m", hatch="/")
plt.title("long graph")
plt.plot(x, y3, "r:", label="long Graph")
plt.xlabel("x", color="b")
plt.ylabel("y", color="b")
plt.legend(edgecolor="y")
plt.text(2, 2, "text 2", color="blue", rotation="vertical", bbox=bbox_3)
plt.annotate(
    "annotate text",
    xy=(4, 3),
    xytext=(6, 7),
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="angle, angleA=70, angleB=30, rad=0.0",
        facecolor="g",
    ),
)  # facecolor='green', shrink=0.05,
plt.grid()

plt.show()
