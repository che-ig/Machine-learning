import matplotlib.pyplot as plt
import numpy as np

# fill_between - закрашенная область между линиями.
fig, ax = plt.subplots(2, 1)
x = np.linspace(0, 10, 10)

y1 = x + 2
y2 = x
ax[0].fill_between(x, y1, y2)

y3 = 1.5 * x + 10
y4 = 4 * x + 10
ax[0].fill_between(x, y3, y4)

# Указанные линии могут пересекать друг друга.
a = np.linspace(-10, 10, 100)
b1 = a**2
b2 = a**2 - 20 * np.cos(a)
ax[1].fill_between(a, b1, b2)

fig.set(facecolor="floralwhite", figwidth=12, figheight=9)
ax[0].set(facecolor="seashell")

# Если линии пересекаются, то с помощью параметра where можно указать выше
# или ниже какой линии должна закрашиваться область, а с помощью параметра
# facecolor можно задать ее цвет.

fig2, ax2 = plt.subplots(2, 1)

c = np.linspace(-12, 12, 200)
d = c**2
d1 = c**2 - 40 * np.cos(c)

ax2[0].plot(c, d, color="r", linewidth=2)
ax2[0].plot(c, d1, color="b", linewidth=3)

ax2[0].fill_between(c, d, d1, where=(d1 > d), facecolor="yellow")
ax2[0].fill_between(c, d, d1, where=(d1 < d), facecolor="black")

# Можно управлять цветом и другими параметрами линии, а также можно установить
# прозрачность всей области.

t = np.linspace(0, 3 * np.pi, 100)
g = np.cos(t)
g1 = np.sin(t)

ax2[1].fill_between(
    t,
    g,
    2 * g + 1,
    facecolor="r",
    alpha=0.5,
    edgecolor="black",
    linewidth=2,
    linestyle="--",
)
ax2[1].fill_between(
    t,
    g1,
    3 * g1,
    facecolor="g",
    alpha=0.5,
    edgecolor="black",
    linewidth=2,
    linestyle="--",
)

fig2.set(facecolor="floralwhite", figwidth=12, figheight=12)
plt.show()
