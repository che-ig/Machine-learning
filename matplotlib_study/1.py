from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
y = x
y2 = [i**2 for i in x]

# first graph
plt.figure(figsize=(9, 9))

plt.subplot(2, 2, 1)
plt.plot(x, y, "rx", label="first graph")
plt.title("Linear dependence y = x")
plt.ylabel("y", fontsize=14)  # axis y
plt.grid()  # add grid
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, y2, "g--")  # create graph
plt.xlabel("x", color="blue")  # axis x
plt.ylabel("y2", fontsize=14)  # axis y
plt.text(5, 80, "my notice", color="red")  # the text on the graph
plt.grid()  # add grid

plt.subplot(2, 2, 3)
fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts, label="All fruits")
plt.title("Fruits")
plt.xlabel("Count", color="blue")
plt.ylabel("fruit", color="blue")
plt.legend()

plt.show()
