import matplotlib.pyplot as plt
import numpy as np

# Stackplot - надставленные области
# Данный график очень похож на fill_between, но в отличии от него, он может
# создавать области между несколькими линиями и позволяет определить как эти
# области должны выравниваться относительно др. др.

x = [0, 1, 2, 3, 4, 5]
y = [2, 6, 4, 8, 2, 4]
y2 = [2, 4, 2, 4, 4, 10]

# Фактические координаты: y2 = [4, 10, 6, 12, 6, 14]
fig, ax = plt.subplots()

ax.stackplot(x, [y, y2])
fig.set(facecolor="floralwhite", figwidth=12, figheight=6)
ax.set(facecolor="seashell")

# Это лишь один пример с pyprog

plt.show()
