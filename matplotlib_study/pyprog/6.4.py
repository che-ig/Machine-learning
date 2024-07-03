import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3 * np.pi, 3 * np.pi, 200)
y = np.sinc(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()

fig_2 = plt.figure(figsize=(12, 12))
ax_1 = fig_2.add_subplot(2, 1, 1)
ax_2 = fig_2.add_subplot(2, 2, 3)
ax_3 = fig_2.add_subplot(2, 2, 4)

# Линии сетки бывают как основные так вспомогательные.
# За их отображение отвечает параметр which

# Данный параметр может принимать одно из трех значений:
# 'major' - применение параметров внешнего вида к основным линиям (установлен по умолчанию);
# 'minor' - к вспомогательным линиям;
# 'both' - к обеим линиям.
ax_1.plot(x, y)

# Прежде чем рисовать вспомогательные линии сетки
# необходимо включить второстепенные деления.
ax_1.minorticks_on()

# Внешний вид основной линии
ax_1.grid(which="major", color="r", linewidth=1)

# Внешний вид вспомогательной линии
ax_1.grid(which="minor", color="g", linestyle="-.")
ax_1.set(title='axis="both"')

ax_2.plot(x, y, linewidth=3)
ax_2.grid(
    axis="y",  # Ось по которой будет нарисована сетка
    color="b",  # Цвет линии сетки
    linewidth="2",  # Толщина линии сетки
    linestyle="--",
)  # Стиль линии
ax_2.set(title='axis="y"')

ax_3.plot(x, y, color="k", linewidth=3)
ax_3.grid(axis="x")
ax_3.set(title="x")

plt.show()
