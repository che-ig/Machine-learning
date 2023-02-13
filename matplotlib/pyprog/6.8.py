import matplotlib.pyplot as plt
# Подключаем модуль управления тиками
import matplotlib.ticker as ticker
import numpy as np

x = np.linspace(-10, 10, 200)
y = 0.02 * (x + 9) * (x + 6) * (x - 6) * (x - 9) * x

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].plot(x, y, color='r', linewidth=3)

# Устанавливаем интервал основных и вспомогательных делений.
ax[0].xaxis.set_major_locator(ticker.MultipleLocator(2))
ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax[0].yaxis.set_major_locator(ticker.MultipleLocator(50))
ax[0].yaxis.set_minor_locator(ticker.MultipleLocator(10))

# Добавим линии основной сетки
ax[0].grid(which='major', color='k')

# Включим видимость вспомогательных делений
ax[0].minorticks_on()

# Теперь можнем отдельно задать внешний вид вспомогательной сетки.
ax[0].grid(which='minor', color='gray', linestyle=':')

ax[1].plot(x, y, color='r', linewidth=3)
# Устанавливаем интервал основных и вспомогательных делений.
ax[1].xaxis.set_major_locator(ticker.MultipleLocator(2))
ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(100))
ax[1].yaxis.set_minor_locator(ticker.MultipleLocator(10))

# Настраиваем вид основных тиков.
ax[1].tick_params(
    axis='both',  # Применяем параметры к обеим осям
    which='major',  # Применяем параметры к основным делениям
    direction='in',  # Рисуем деления внутрь
    length=10,  # Длина деления
    width=4,  # Ширина деления
    color='m',  # Цвет деления
    pad=10,  # Расстояние между черточкой и ее подписью
    labelsize=15,  # Размер подписи
    labelcolor='r',  # Цвет подписи
    bottom=True,  # Рисуем метки снизу
    left=True,  # Слева
    right=True,  # Справа
    labelbottom=True,  # Рисуем подписи снизу
    labelleft=True,  # Рисуем подписи слева
    labelright=True,  # Рисуем подписи справа
    labelrotation=45  # Поворот подписей
)

ax[1].tick_params(
    axis='both',  # Применяем параметры к обеим осям
    which='minor',  # Применяем параметры к основным делениям
    direction='in',  # Рисуем деления внутрь
    length=5,  # Длина деления
    width=2,  # Ширина деления
    color='m',  # Цвет деления
    pad=10,  # Расстояние между черточкой и ее подписью
    labelsize=15,  # Размер подписи
    labelcolor='r',  # Цвет подписи
    bottom=True,  # Рисуем метки снизу
    left=True,  # Слева
    right=True  # Справа
)

ax[1].minorticks_on()
ax[1].grid(which='minor', color='m', linestyle=':')
plt.show()
