import matplotlib.pyplot as plt

# Создаем главный контейнер для всех графиков.
fig = plt.figure(layout='constrained')

# Создаем отдельную область с графиком.
ax_1 = fig.add_subplot(3, 2, 1)

fig.set_facecolor('green')

ax_1.set_facecolor('red')
ax_1.set_xlim([-10, 10])
ax_1.set_ylim([-2, 2])
ax_1.set_title('Основы анатомии matplotlib')
ax_1.set_xlabel('Ось абсцис (Xax_1is)')
ax_1.set_ylabel('Ось ординат (YAis)')

# Метод set есть практически у всех объектов matplotlib.
# Например, нам вдруг захотелось изменить цвет и размер title. Для этого существуют так же два способа:

# Способ 1:
ax_1.set_title('Основы анатомии matplotlib', color='white', size=20)

# Способ 2:
ax_1.set_title('Основы анатомии matplotlib')
ax_1.title.set_color('white')
ax_1.title.set_size(20)

# Добавит простые графики - линейный и точечный
ax_2 = fig.add_subplot(3, 2, 2)
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_2.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19])
ax_2.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27])

ax_3 = fig.add_subplot(3, 2, 4)
ax_3.set(title='ax_3', xticks=[], yticks=[])
ax_3.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], color='black', linewidth=5)
ax_3.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27],
             color='blue',
             marker='*',
             linewidth=3)

ax_4 = fig.add_subplot(3, 3, 8)
ax_4.set(title='ax_4', xticks=[], yticks=[])

###########################
# Более удобный способ разбивки

# fig_2 - это область Figure
# axes - это массив numpy
fig_2, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set(title='axes[0, 0]')
axes[0, 1].set(title='axes[0, 1]')
axes[1, 0].set(title='axes[1, 0]')
axes[1, 1].set(title='axes[1, 1]')

for ax in axes.flat:
    ax.set(xticks=[], yticks=[])

plt.show()
