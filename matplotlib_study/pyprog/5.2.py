import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.random.rand(100)
y = np.random.rand(100)

# Установим ширину и высоту фигуры
fig.set(figwidth=8, figheight=8)

# Это сам график
ax.scatter(x, y, c="deeppink")

# Это настройки области графика
ax.set(facecolor="black", title="Один цвет")

# Если нужно на одном графике разместить несколько наборов данных,
# то каждый набор должен иметь свой цвет.

fig_2, ax_2 = plt.subplots()

x1 = np.random.rand(300)
y1 = np.random.gamma(1, size=300)
y2 = np.random.gamma(2, size=300)
y3 = np.random.gamma(4, size=300)
y4 = np.random.gamma(8, size=300)

# Базовые опции scatter:
# c - цвет
# s - размер маркера

# Ключ цвета из (b, g, r, c, m, y, k, w)
ax_2.scatter(x1, y1, c="r", s=1)

# RGB
ax_2.scatter(x1 + 1, y2, c=[[0.1, 0.63, 0.55]], s=2)

# hex RGB
ax_2.scatter(x1 + 2, y3, c="#ad09a3", s=4)

# Уровень серого в интервале [0, 1]
ax_2.scatter(x1 + 3, y4, c=["0.9"], s=8)

ax_2.set(facecolor="black", title="Цвет указывает на принадлежность к данным")
fig_2.set(figwidth=8, figheight=8)

# Когда хотим подкрасить каждый маркер в свой цвет

fig_3, ax_3 = plt.subplots(1, 2)
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

ax_3[0].scatter(a, b, c=["r", "g", "b", "w"], marker="s", s=100)
ax_3[0].set(facecolor="black", title="Цвет каждой точки по строке-ключа")

# Цвета из встроенной палитры
ax_3[1].scatter(a, b, c=[0.9, 0.8, 0.7, 0.6], marker="*", s=200)
ax_3[1].set(facecolor="black", title="Цвета из встроенной палитры")

# Благодаря numpy мы можем очень легко задать цвет каждой точке
# и закрасить их по определенному правилу.

fig_4, ax_4 = plt.subplots(4, 1)

a1 = np.random.rand(100)
b1 = np.random.rand(100)
colors = np.random.rand(100)

size_for_markers = np.random.randint(1, 300, 100)
ax_4[0].scatter(a1, b1, c=colors, marker="o", edgecolor="white", s=size_for_markers)

# Цвет каждой точки из палитры по умол-ю
ax_4[0].set(
    facecolor="black", title="Цвет каждой точки из палитры по умол-ю", xticks=[]
)  # xticks - это метки на шкале по оси x

# RGB цвет каждой точки
rgb = np.random.rand(100, 3)
ax_4[1].scatter(a1, b1, color=rgb)
ax_4[1].set(facecolor="black", title="RGB цвет каждой точки")

# RGBA цвет каждой точки
rgba = np.random.rand(100, 4)
ax_4[2].scatter(a1, b1, color=rgba)
ax_4[2].set(facecolor="black", title="RGBA цвет каждой точки")

# Создаем массив по определенному правилу с помощью логических операций
# и индексации массивов массивами булевых значений.
col = np.empty_like(b1)
below_points = b1 < 0.5  # скобки нужны для читабельности
upper_points = b1 >= 0.5
col[below_points] = 0.2
col[upper_points] = 0.6

ax_4[3].scatter(a1, b1, c=col)
ax_4[3].set(
    facecolor="black",
    title="Два цвета для точек выше и ниже 0.5",
    xticks=[],
    yticks=[0, 0.5, 1],
)

# Ширина и высота figure
fig_4.set(figwidth=12, figheight=12, constrained_layout=True)

plt.show()
