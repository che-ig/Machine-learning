import inspect
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

np.random.seed(42)
xy = []
for i in range(7):
    bxy, bc = make_blobs(n_samples=100, centers=1, n_features=2, cluster_std=2)
    xy.append(bxy)
colors = ("red", "blue", "green", "yellow", "pink", "gray", "aqua")
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# for i in range(7):
#     plt.scatter(xy[i][:, 0], xy[i][:, 1], c='brown')

# plt.subplot(1, 2, 2)
# for i in range(7):
#    plt.scatter(xy[i][:, 0], xy[i][:, 1], c=colors[i])

xy_points = []
scatter_x = []
scatter_y = []
for i in xy:
    xy_points.extend(i)
    scatter_x.extend(i[:, 0])
    scatter_y.extend(i[:, 1])
# special_predict
# xy_points.extend([[0, 0]])
# scatter_x.append(0)
# scatter_y.append(0)
plt.figure(figsize=(10, 10))
for num_clusters in range(2, 11):
    kMeans = KMeans(n_clusters=num_clusters)
    kMeans.fit(xy_points)
    predictions = kMeans.predict(xy_points)
    clrs = [colors[p % len(colors)] for p in predictions]
    plt.subplot(3, 3, num_clusters - 1)
    plt.scatter(scatter_x, scatter_y, c=clrs, edgecolors="none")
    # plt.xticks([],[])
    # plt.yticks([],[])
    plt.title(str(num_clusters) + " clusters")

plt.show()
