import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
from sklearn import linear_model

np.random.seed(42)
ridge_estimator = linear_model.Ridge()

num_pts = 100
nouse_range = 0.2
x_vals = []
y_vals = []
zzz = []
(x_left, x_right) = (-2, 2)
for i in range(num_pts):
    x = np.random.uniform(x_left, x_right)
    y = np.random.uniform(-nouse_range, nouse_range) + (2 * math.sin(x))

    x_vals.append(x)
    y_vals.append(y)
    zzz.append([x, y])

x_column = np.reshape(x_vals, (len(x_vals), 1))

plt.figure(figsize=(10, 4))

ridge_estimator.fit(x_column, y_vals)

y_left = ridge_estimator.predict(np.array([[x_left]]))
y_right = ridge_estimator.predict(np.reshape([x_right], [-1, 1]))

plt.subplot(1, 2, 1)
plt.scatter(x_vals, y_vals)
plt.plot([x_left, x_right], [y_left, y_right], "o-.r")
plt.title("original data with best line")

plt.subplot(1, 2, 2)
plt.scatter(x_vals, y_vals)
plt.title("original data")

plt.show()
