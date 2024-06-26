import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 8)
y = np.random.randint(1, 20, size=7)

x1 = np.arange(1, 101)
y1 = np.random.randint(1, 20, size=100)

fig, ax = plt.subplots(2, 1)
ax[0].bar(x, y, color='r')
ax[1].bar(x1, y1, color='b')

ax[0].set(facecolor='seashell')
ax[1].set(facecolor='seashell')
fig.set(facecolor='floralwhite', figwidth=12, figheight=6)

# Когда необходимо отобразить несколько наборов данных на одной Axes
# Специально делаем смещение в +- 0.2 потому что ниже делаем ширину равную 0.4
a1 = np.arange(1, 8) - 0.2
a2 = np.arange(1, 8) + 0.2
b1 = np.random.randint(1, 10, size=7)
b2 = np.random.randint(1, 10, size=7)

fig_2, ax_2 = plt.subplots()

# При желании можно задать ширину каждого из столбцов
width_rectangle = 0.1 * np.random.randint(1, 4, size=7)

ax_2.bar(a1, b1, width=0.4)
ax_2.bar(a2, b2, width=width_rectangle)

ax_2.set(facecolor='seashell')
fig_2.set(facecolor='floralwhite', figwidth=12, figheight=6)

# Выравнивание нижнего края прямоугольника
# Разместить несколько гистограмм на одной области Axes можно не только с
# помощью горизонтального смещения и изменения ширины прямоугольников, но и
# с помощью параметра bottom.
fig_3, ax_3 = plt.subplots()

t = np.arange(1, 8)
k1 = np.random.randint(1, 10, size=7)
k2 = np.random.randint(1, 10, size=7)
k3 = np.random.randint(1, 10, size=7)

ax_3.bar(t, k1)
ax_3.bar(t, k2, bottom=11, color='r')
ax_3.bar(t, k3, bottom=21, color='y')

ax_3.set(facecolor='seashell')
fig_3.set(facecolor='floralwhite', figwidth=12, figheight=6)

# Для того чтобы состыковать прямоугольники нескольких наборов данных,
# достаточно выровнять одни прямоугольники по значениям других.
p = np.arange(1, 8)
data_1 = np.random.randint(2, 15, size=7)
data_2 = np.random.randint(3, 20, size=7)

fig_4, ax_4 = plt.subplots()
ax_4.bar(p, data_1)
ax_4.bar(p, data_2, bottom=data_1)

# matplotlib поддерживает возможность задания цвета через разные цветовые
# модели и форматы.
fig_5, ax_5 = plt.subplots()
colors_rgb = np.random.rand(7, 3)
colors_rgba = np.random.rand(7, 4)

# Дополнительно выделим границу прямоугольника и зададим ей свою ширину.
ax_5.bar(p, data_1, color=colors_rgb, edgecolor='g', linewidth=3)
ax_5.bar(p, data_2, color=colors_rgba, edgecolor='darkblue', linewidth=3)

ax_5.set(facecolor='seashell')
fig_5.set(facecolor='floralwhite', figwidth=12, figheight=6)

# Отображение погрешности.
# На гистограмме можно указать погрешность измерения величины, как по горизонтали
# (xerr) так и вертикали (yerr)
n = np.arange(1, 8)
date_3 = np.random.randint(1, 10, size=7)
x_errors = np.random.rand(7)
y_errors = np.random.rand(7) * 2

fig_6, ax_6 = plt.subplots(2, 1)
ax_6[0].bar(n, date_3, xerr=x_errors, width=0.3)
ax_6[1].bar(n, date_3, yerr=y_errors, width=0.5)

ax_6[0].set(facecolor='seashell')
ax_6[1].set(facecolor='seashell')

fig_6.set(facecolor='floralwhite', figwidth=12, figheight=6)

# Различные варианты работы с ошибками.
w = np.arange(1, 13)
q = np.random.randint(5, 20, size=12)

fig_7, ax_7 = plt.subplots(4, 1)
ax_7[0].bar(w, q, yerr=1)

y_err = np.random.rand(12) * 5
ax_7[1].bar(w, q, yerr=y_err)

y_err_2 = np.random.rand(2, 12) * 5
y_err_2[:][0] /= 2
ax_7[2].bar(w, q, yerr=y_err_2)

# Линии погрешности так же можно видоизменять.
y_err_3 = np.random.randint(5, 20, size=(2, 12)) / 15
ax_7[3].bar(
    w,
    q,
    yerr=y_err_3,  # границы погрешности
    ecolor='darkred',  # цвет линии погрешности
    capsize=10,  # горизонтальная черта у погрешности
    edgecolor='red',  # цвет границы прямоугольника
    linewidth=2,  # ширина окантовки
    color='seashell',  # цвет прямоугольника
    linestyle='--')  # начертание линии

ax_7[0].set(title='Одинаковая погрешность', facecolor='seashell', xticks=[])
ax_7[1].set(title='Разная, но симметричная погрешность',
            facecolor='seashell',
            xticks=[])
ax_7[2].set(title='Максимальная и минимальная погрешность',
            facecolor='seashell',
            xticks=[])
ax_7[3].set(title='Максимум настроек', facecolor='seashell', xticks=[])

fig_7.set(facecolor='floralwhite', figwidth=12, figheight=12)

plt.show()
