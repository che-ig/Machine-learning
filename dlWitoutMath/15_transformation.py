import numpy as np
from sklearn.datasets import make_moons
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

np.random.seed(42)
moon_data = make_moons(n_samples=100, noise=2)
training_samples = moon_data[0]
train_x = training_samples[:, 0]
train_y = training_samples[:, 1]

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.scatter(train_x, train_y, c="g", ec="none")
plt.title("original data")

mm_scaler = MinMaxScaler()  # создаем преобразователь масштаба
mm_scaler.fit(training_samples)
transform_training_samples = mm_scaler.transform(training_samples)
plt.subplot(2, 2, 2)
plt.scatter(transform_training_samples[:, 0], transform_training_samples[:, 1], c="red")
plt.title("MinMaxScaler transformed data")

test_moon_data = make_moons(n_samples=100, noise=0.05)
test_samples = test_moon_data[0]
test_samples = np.array([[ts[0] * 4, ts[1] * 8] for ts in test_samples])
test_x = test_samples[:, 0]
test_y = test_samples[:, 1]

# mm_scaler.fit(test_samples)
transform_test_samples = mm_scaler.transform(test_samples)

plt.subplot(2, 2, 3)
plt.scatter(test_x, test_y, c="m")
plt.title("test data")

plt.subplot(2, 2, 4)
plt.scatter(transform_test_samples[:, 0], transform_test_samples[:, 1])
plt.plot([0, 1], [0, 0], "g-.", alpha=0.3)
plt.plot([1, 0], [1, 1], "g-.", alpha=0.3)
plt.plot([1, 1], [0, 1], color="black", alpha=0.3)
plt.plot([0, 0], [0, 1], color="black", alpha=0.3)
plt.title("test transformed data")
plt.show()
