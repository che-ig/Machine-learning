from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x
y2 = [i**2 for i in x]

# first graph
plt.figure(figsize=(9, 9))

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Linear dependence y = x')
plt.ylabel('y', fontsize=14) # axis y
plt.grid() # add grid 

plt.subplot(2, 2, 2)
plt.plot(x, y2) # create graph
plt.xlabel('x') # axis x
plt.ylabel('y2', fontsize=14) # axis y
plt.grid() # add grid 
plt.legend()

plt.subplot(2, 2, 3)
fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
counts = [34, 25, 43, 31, 17] 
plt.bar(fruits, counts)
plt.title('Fruits')
plt.xlabel('Count')
plt.ylabel('fruit')

plt.show()