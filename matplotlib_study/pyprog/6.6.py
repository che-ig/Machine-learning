import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = (x - 2) * (x + 2)
y2 = 2 * x + 5

fig, ax = plt.subplots(2, 1, figsize=(12, 8))

ax[0].plot(x, y1)
ax[0].plot(x, y2)

ax[0].text(0, 9, "Прямая", rotation=28, fontsize=18)
ax[0].text(0, -2, "Парабола", rotation=28, fontsize=18)

box_1 = {
    "facecolor": "black",  # Цвет области (заливка)
    "edgecolor": "red",  # Цвет контура
    "boxstyle": "round",  # Геометрическая форма области
}

box_2 = {
    "facecolor": "k",
    "edgecolor": "r",
    "boxstyle": "circle",
    "linestyle": ":",  # Стиль линии
    "linewidth": "3",  # Толщина линии
}

box_3 = {
    "facecolor": "black",
    "edgecolor": "red",
    "boxstyle": "rarrow",
    "pad": 0.9,  # Отступ
}

ax[1].text(0.1, 0.5, "Мой текст", bbox=box_1, color="white", fontsize=20)  # Цвет текста

ax[1].text(
    0.5,
    0.35,
    "Мой первый текст",
    horizontalalignment="center",  # Горизонтальное выравнивание
    bbox=box_2,
    color="white",  # Цвет текста
    fontsize=20,
)

ax[1].text(
    0.7, 0.5, "Мой первый текст", bbox=box_3, color="white", fontsize=20  # Цвет текста
)

plt.show()
