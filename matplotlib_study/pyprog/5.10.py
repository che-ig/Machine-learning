import matplotlib.pyplot as plt
import numpy as np

# Arrow - стрелка.
# Если необходимо сфокусировать внимание на определенном участке графика -
# то можно отметить его стрелкой.

x = np.linspace(-5, 5, 100)
y = x * (x - 4) * (x + 4)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.arrow(-2.3, 0, 0, 20, width=0.1, head_length=4)
ax.arrow(2.3, 0, 0, -20, width=0.1, head_length=4)

fig.set(figwidth=12, figheight=4)

# Примеры отображения.
# В самом простом случае стрелка задается всего 4 параметрами.
# x, y - координаты начала стрелки
# dx, dy- длина стрелки по оси x, y
fig2, ax2 = plt.subplots(2, 1)
ax2[0].arrow(0.1, 0.3, 0.7, 0.3)
# Чтобы линия превратилась в стрелку нужно задать небольшое зн. width.
ax2[1].arrow(0.1, 0.3, 1.3, 1.7, color="r", width=0.05, head_length=1)

# Длина стрелки будет включать в себя длину острия length_includes_head
# head_width - ширина острия стрелки
# head_length - длина острия стрелки
# shape - мы можем выбирать форму стрелки
# color - задает цвет стрелки
# linestyle - начертание линии
# linewidth - ширина линии
ax2[1].arrow(
    0.1,
    0.9,
    1.3,
    1.7,
    width=0.05,
    length_includes_head=True,
    head_width=0.6,
    head_length=0.5,
    shape="left",
    color="r",
    linestyle="--",
    linewidth=3,
)
ax2[1].set(xticks=[0, 1, 2, 3], yticks=[0, 1, 2, 3])
plt.show()
