import numpy as np
from matplotlib import pyplot as plt
rnd = np.random.randint

cat_par = [f'P{i}' for i in range(5)]
g1 = [10, 21, 34, 12, 27]
g2 = [17, 15, 25, 21, 26]
width = 0.3
x = np.arange(len(cat_par))
fig, ax = plt.subplots()
error = np.array([[rnd(2, 7), rnd(2, 7)] for _ in range(len(cat_par))]).T
rects1 = ax.bar(x - width/2, g1, width, label='g1')
rects2 = ax.bar(x + width/2, g2, width, label='g2', color='y', alpha=0.5,
                yerr=error, ecolor='m')
ax.set_title('Пример групповой диаграммы')
ax.set_xticks(x)
ax.set_xticklabels(cat_par)
ax.legend()
print(error)
plt.show()