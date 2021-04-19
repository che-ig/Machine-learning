import numpy as np
from sklearn.datasets import make_moons
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

np.random.seed(11)
moon_data = make_moons(n_samples=100, noise=2)
training_samples = moon_data[0]
train_x = training_samples[:, 0]
train_y = training_samples[:, 1]

plt.figure(figsize=(8, 5))

plt.subplot(1, 2, 1)
plt.scatter(train_x, train_y, c='g', ec='none')
plt.title('original data')

mm_scaler = MinMaxScaler()  # создаем преобразователь масштаба
mm_scaler.fit(training_samples)
transform_training_samples = mm_scaler.transform(training_samples)
plt.subplot(1, 2, 2)
plt.scatter(transform_training_samples[:, 0], transform_training_samples[:, 1], c='red')
plt.title('MinMaxScaler transformed data')
plt.show()