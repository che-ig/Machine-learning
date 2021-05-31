import numpy as np
from sklearn.datasets import make_moons
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

np.random.seed(42)
test_moon_data = make_moons(n_samples=100, noise=0.05)

mm_scaler = MinMaxScaler()  # создаем преобразователь масштаба

test_samples = test_moon_data[0]
test_samples = np.array([[ts[0]*2, ts[1]*.6] for ts in test_samples])
test_x = test_samples[:,0]
test_y = test_samples[:,1]

transformed_test_samples = mm_scaler.transform(test_samples)

plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
plt.scatter(test_x, test_y, color='#7F3900', s=40)
plt.title('test data')

plt.subplot(1, 2, 2)
plt.scatter(transformed_test_samples[:,0], transformed_test_samples[:,1], color='#7F3900', s=10)
plt.plot([0,1], [0,0], color='black')
plt.plot([1,1], [0,1], color='black')
plt.plot([0,1], [1,1], color='black')
plt.plot([0,0], [0,1], color='black')
plt.title("MinMaxScaler transformed test data")

plt.show()