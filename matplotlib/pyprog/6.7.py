import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
y = x * (x - 3) * (x - 4)

fig, ax = plt.subplots(2, 1, figsize=(8, 12))
ax[0].plot(x, y)
ax[0].grid()

# Добавить подписи к осям.
ax[0].set_xlabel('время (с)')
ax[0].set_ylabel('скорость (м/c)')

# Методы set_xlabel и set_ylabel как и метод Axes.text(), принимает целый ряд
# параметров, отвечающих за отображение текста.
ax[1].plot(x, y)
ax[1].set_xlabel(
    'время (с)',
    fontsize=15,  # Размер шрифта
    color='red',  # Цвет шрифта
    # Параметры области текста
    bbox={
        'boxstyle': 'rarrow',  # Форма области
        'pad': 0.1,  # Отступы вокруг текста
        'facecolor': 'white',  # Цвет заливки области
        'edgecolor': 'red',  # Цвет рамки
        'linewidth': 2  # Ширина линии
    })

ax[1].set_ylabel(
    'скорость (м/с)',
    fontsize=15,  # Размер шрифта
    color='red',  # Цвет шрифта
    # Параметры области текста
    bbox={
        'boxstyle': 'rarrow',  # Форма области
        'pad': 0.1,  # Отступы вокруг текста
        'facecolor': 'white',  # Цвет заливки области
        'edgecolor': 'red',  # Цвет рамки
        'linewidth': 2  # Ширина линии
    })

plt.show()
