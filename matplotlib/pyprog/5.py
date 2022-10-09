import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# На одной области Axes можно отобразить несколько наборов данных.
# Данные которые хотим отобразить
x1 = np.linspace(0, 10, 30)
y1 = np.random.beta(0.1, 0.6, size=30)

x2 = np.linspace(11, 20, 30)
y2 = 10 * np.random.gamma(shape=0.3, scale=1.1, size=30)

x3 = np.linspace(21, 30, 30)
y3 = 10 * np.random.pareto(3.5, size=30)

# Данные в виде точек
ax.scatter(x1, y1)
ax.scatter(x2, y2)
ax.scatter(x3, y3)

# Данные в виде линии
ax.plot(x1, y1 + 3)
ax.plot(x2, y2 + 3)
ax.plot(x3, y3 + 3)

ax.set(title='Бета, Гамма, Паретто распределения')

####################################################

# В случае когда у нас несколько областей Axes, то отображение на них данные
# можно реализовать двумя способами: add_subplot() и subplots()

x4 = np.linspace(0, 10, 100)
y4 = np.sin(x4)
img = y4.reshape(5, 20)

# Создаем фигуру
fig_2 = plt.figure()

# Создаем 2 области для графиков
ax_1 = fig_2.add_subplot(2, 1, 1)
ax_2 = fig_2.add_subplot(2, 1, 2)

# Методы для отображения данных
ax_1.plot(x4, y4)
ax_2.imshow(img)

# Добавляем заголовки к Axes
ax_1.set(title='sin(x)')
ax_2.set(title='img')

# Альтернатива с помощью subplots (получим тоже самое что и выше)
fig_2, ax_4 = plt.subplots(nrows=2, ncols=1)

# Методы отображения данных
ax_4[0].plot(x4, y4)
ax_4[1].imshow(img)

ax_4[0].set(title='sin(x)')
ax_4[1].set(title='img')

plt.show()
