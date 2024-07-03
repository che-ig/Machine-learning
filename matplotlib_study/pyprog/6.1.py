import matplotlib.pyplot as plt
import numpy as np

# Добавить заголовок к области Axes можно с помощью метода set_title
data = np.random.normal(0, 1, 1000)
fig, ax = plt.subplots()

ax.hist(data, bins=50, rwidth=0.4)
ax.set_title("Нормальное распределение")

# Параметры loc и pad позволяют быстро задать гор. и верт. выравнивание.
fig2, ax2 = plt.subplots(1, 3)

for ax in ax2:
    mu = 10 * np.random.random()
    kappa = 10 * np.random.random()
    data = np.random.vonmises(mu, kappa, size=1000)
    ax.hist(data, bins=50, rwidth=0.4)

# Вертикальное и гор. выравнивание заголовков.
ax2[0].set_title(
    'loc = "left", pad = 0',
    fontsize=20,  # Рзазмер шрифта
    color="red",  # Цвет заголовка
    backgroundcolor="black",  # Цвет фона заголовка
    loc="left",
    pad=0,
)  # Задает расстояние в точках.

ax2[1].set_title(
    'loc ="center", pad = 10', loc="center", pad=10  # Значение по умолчанию
)

ax2[2].set_title('loc = "right", pad = 20', loc="right", pad=20)

# Заголовок области фигуры
fig2.suptitle("Заголовок области фигуры", y=1.2, fontsize=20)

fig2.set(figheight=4, figwidth=14)

plt.show()
