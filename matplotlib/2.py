from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1, 20)
y = x * 2
y2 = [i*1.5 for i in y]
y3 = [i*1.7 for i in y2]
y4 = [i*1.7 for i in y3]

flg, axs = plt.subplots(2, 2, figsize=(12, 7))
axs[0, 0].plot(x, y, 'r--')
axs[0, 1].plot(x, y2, 'b:')
axs[1, 0].plot(x, y3, 'g-.')

plt.title('my title')
axs[1, 1].plot(x, y4, 'rx')

plt.show()