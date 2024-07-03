import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3 * np.pi, 3 * np.pi, 200)
y1 = np.sin(x) - 2
y2 = np.sin(x) + 2
y3 = np.sinc(x)

fig, ax = plt.subplots()
# Текст легенды задается в параметре label для каждого графика индивидуально
ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")
ax.plot(x, y3, label=r"$\frac{sin(x)}{x}$")

# Без принудетельного вызова этого метода легенда не появится
ax.legend()
fig.set(figwidth=8, figheight=5)

# ==================================================

fig_2, axes = plt.subplots(5, 2, figsize=(10, 10))
# Все возможные значения расположения легенды
location = [
    "upper right",
    "upper left",
    "lower left",
    "lower right",
    "right",
    "center left",
    "center right",
    "lower center",
    "upper center",
    "center",
]
i = 0
for ax in axes.ravel():
    shadow = True if i % 2 == 1 else False
    ax.plot(x, y1, label="sin(x)")
    ax.legend(loc=location[i], fontsize=14, shadow=shadow)
    ax.set(title=location[i], xticks=[], yticks=[])
    i += 1

# ==================================================
xx = np.linspace(-5, 5, 10)
z1 = 2 * xx + 5
z2 = -xx + 8
z3 = 0.5 * xx + 5
# full создает в данном случае массив с десятью значениями 5
z4 = np.full(10, 5)
fig_3, ax_3 = plt.subplots(figsize=(12, 12))

ax_3.plot(xx, z1, label="y = 2x + 5")
ax_3.plot(xx, z2, label="y = -x + 8")
ax_3.plot(xx, z3, label="y = 0.5x + 5")
ax_3.plot(xx, z4, label="y = 5")

ax_3.legend(
    fontsize=15,
    ncol=2,  # Количество столбцов в легенде
    facecolor="oldlace",  # Цвет области
    edgecolor="r",  # Цвет рамки
    title="Прямые",  # Заголовок
    title_fontsize=20,  # Размер шрифта заголовка
)

plt.show()
