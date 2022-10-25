import matplotlib.pyplot as plt
import numpy as np

# Цвет линии

x = np.zeros(8)
fig, ax = plt.subplots()

# RGB
ax.plot(x, color=(0.9, 0.2, 0.9))

# RGBA
ax.plot(np.arange(-1, 7), color=(0.9, 0.2, 0.9, 0.5), linewidth=12)

# hex RGB
ax.plot(x + 1, color='#0a0b0c')

# hex RGBA
ax.plot(x + 2, color='#0a0b0c3a')

# Уровень серого в интервале [0, 1]
ax.plot(x + 3, color='0.3')

fig.set(facecolor='mintcream', figwidth=12, figheight=6)
ax.set(facecolor='whitesmoke')

# Эксперименты со стилем линии linestyle

fig_2, ax_2 = plt.subplots()
a = np.linspace(-5, 5, 100)
b = np.sin(a)

# Сплошная линия '-' или solid
ax_2.plot(a, b, linestyle='-', linewidth=1, color='crimson')

# Пунктирная линия '--' или dashed
ax_2.plot(a, b + 1, linestyle='--', linewidth=2, color='darkmagenta')

# Точка-тире '-.' или dasdot
ax_2.plot(a, b + 2, linestyle='-.', linewidth=3, color='indigo')

# Точка-точка ':' или dotted
ax_2.plot(a, b + 3, linestyle=':', linewidth=4, color='darkblue')

fig_2.set(figwidth=12, figheight=6, facecolor='linen')
ax_2.set(facecolor='ivory')

# Эксперименты со стилем маркера - marker, markersize
fig_3, ax_3 = plt.subplots()
z = np.zeros(10)

# Вид маркера и размер маркера
ax_3.plot(z, marker='o', color='seagreen')
ax_3.plot(z + 1, marker='^', markersize=10, color='seagreen')
ax_3.plot(z + 2, marker='s', markersize=15, color='seagreen')
ax_3.plot(z + 3, marker='x', markersize=20, color='seagreen')

# Цвет маркера - markerfacecolor
# его края - markeredgecolor
# толщина его края - markeradgewidth

ax_3.plot(z + 5,
          marker='^',
          markersize=20,
          markerfacecolor='lawngreen',
          markeredgecolor='darkgreen',
          markeredgewidth=3,
          color='green')

ax_3.plot(z + 6,
          linewidth=4,
          marker='s',
          markersize=20,
          markerfacecolor='lawngreen',
          markeredgecolor='darkgreen',
          markeredgewidth=5,
          color='lime')

ax_3.plot(z + 7,
          marker='x',
          markersize=20,
          markerfacecolor='lawngreen',
          markeredgecolor='darkgreen',
          markeredgewidth=3,
          color='teal')

fig_3.set(figwidth=12, figheight=6, facecolor='floralwhite')
ax_3.set(facecolor='seashell')
plt.show()
