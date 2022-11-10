"""Модуль, реализующий алгоритм kmeans."""

from __future__ import annotations

import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs, make_classification
from sklearn.metrics.pairwise import euclidean_distances

X, y = make_blobs(n_samples=200, centers=4, cluster_std=2.5, random_state=42)

plt.figure(figsize=(8, 8))
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


class KMeans:
    """Класс, реализующий алгоритм kmeans."""
    def __init__(self: KMeans,
                 X,
                 k: int,
                 *,
                 init_method: str = 'kmeans++',
                 track_history: bool = False) -> None:
        """Метод инициализации класса."""
        self.X = X
        self.k = k
        self.init_method = init_method
        self.track_history = track_history
        self.iters_count = 0
        self.centroids = []

    def train(self: KMeans) -> None:
        """Метод, отвечающий за обучение kmeans."""
        if self.init_method == 'kmeans++':
            self.init_kmeans_pp()
        else:
            self.centroids = self.X[np.random.choice(len(self.X), self.k)]

        if self.track_history:
            self.history = {'centroids': [self.centroids], 'clusters': []}

        has_converted = False

        while not has_converted:
            clusters_assignment = self.assign_clusters()
            new_centroids = self.move_centroids(clusters_assignment)

            # Если разница между вновь подсчитанными центроидами и
            # центроидами на предыдущей итерации меньше 1e-5 то выходим из цикла.
            has_converted = np.linalg.norm(new_centroids -
                                           self.centroids) < 1e-5
            self.centroids = new_centroids
            self.iters_count += 1

            # На каждом шаге пересчета центроидов сохраняем текущие
            # центроиды и разметку данных.
            if self.track_history:
                self.history['centroids'].append(self.centroids)
                self.history['clusters'].append(clusters_assignment)

            # 100 итераций вполне достаточно чтобы прекратить обучение
            # если не выйдем по условию веше.
            if self.iters_count > 100:
                break

        if self.track_history:
            print(f'Алгоритм сошелся за {self.iters_count} итераций.')

    def assign_clusters(self: KMeans):
        """Присваиваем метки данным, согласно их близости к центроидам."""
        return np.array([
            np.argmin(np.linalg.norm(x - self.centroids, axis=1))
            for x in self.X
        ])

    def evaluate(self: KMeans) -> float:
        """Высчитываем сумму расстояний от центроида до его меток."""
        cluster_assignment = self.assign_clusters()
        sum_distance_in_centroid = 0
        for k in range(self.k):
            cluster = self.X[cluster_assignment == k]
            sum_distance_in_centroid += np.sum(
                np.linalg.norm(self.centroids[k] - cluster, axis=1))
        return sum_distance_in_centroid

    def move_centroids(self: KMeans, clusters_assignment):
        """Пересчитываем центроиды."""
        # Путем усреднения всех меток, входящих в центроид мы получаем
        # усредненную метку - она и становится центроидом.
        new_centroids = np.zeros_like(self.centroids)
        for i in range(self.k):
            cluster = self.X[np.equal(clusters_assignment, i)]
            new_centroids[i] = np.mean(cluster, axis=0)
        return new_centroids

    def init_kmeans_pp(self: KMeans):
        """Инициализация центроид по методу kmeans++."""
        # Рандомно инициализируем ПЕРВЫЙ центроид.
        centroids = [self.X[np.random.randint(0, len(X) - 1)]]

        # Инициализируем оставшиеся k - 1 центроид.
        for c_id in range(self.k - 1):

            # Сохраняем для каждой точки минимальное расстояние для текущих
            # центроид. Т.е мы для каждой точки данных высчитываем расстояние
            # до каждого центроида и по итогу сохраняем наименьшее.
            dist = []
            for i in range(self.X.shape[0]):
                point = self.X[i, :]
                d = sys.maxsize

                # Вычисляем мин. расстояние от кущей точки до всех центроид.
                for j in range(len(centroids)):
                    temp_dist = np.linalg.norm(point - centroids[j])
                    d = min(d, temp_dist)
                dist.append(d)

            # Переводим обычный массив в numpy
            dist = np.array(dist)
            # Из всех расстояний берем наибольшее.
            next_centroid = self.X[np.argmax(dist), :]
            centroids.append(next_centroid)
            dist = []
            # self.pplot(self.X, np.array(centroids))

        self.centroids = np.array(centroids)

    def pplot(self, data, centroids):
        plt.scatter(data[:, 0],
                    data[:, 1],
                    marker='.',
                    color='gray',
                    label='data points')
        plt.scatter(centroids[:-1, 0],
                    centroids[:-1, 1],
                    color='black',
                    label='previously selected centroids')
        plt.scatter(centroids[-1, 0],
                    centroids[-1, 1],
                    color='red',
                    label='next centroid')
        plt.title('Select % d th centroid' % (centroids.shape[0]))

        plt.legend()
        plt.show()


if __name__ == '__main__':
    kmeans = KMeans(X, 4, init_method='kmeans++', track_history=True)
    kmeans.train()

    # Выведем историю изменения меток и кластеров.
    iters_count = kmeans.iters_count - 1
    fig, ax = plt.subplots(iters_count)
    fig.set(figheight=8 * iters_count, figwidth=8)
    for i in range(iters_count):
        ax[i].scatter(kmeans.X[:, 0],
                      kmeans.X[:, 1],
                      c=kmeans.history['clusters'][i])
        his = kmeans.history['centroids']
        ax[i].scatter(his[i][:, 0], his[i][:, 1], s=100, c='r', marker='x')
    plt.show()

    # Применим метод плеча.
    # Для разных k вычислям сумму расстояний от каждого центроида до
    # каждой точки данных ассоциированной с этим центроидом и смотрим как
    # меняется это расстояниие.
    score = []
    for k in range(2, 8):
        km = KMeans(X, k, init_method='')
        km.train()
        score.append(km.evaluate())
    plt.plot(range(2, 8), score)

    # Выводим итоговый график с размеченными данными.
    plt.figure(figsize=(8, 8))
    plt.scatter(kmeans.X[:, 0], kmeans.X[:, 1], c=kmeans.assign_clusters())
    plt.scatter(kmeans.centroids[:, 0],
                kmeans.centroids[:, 1],
                c='r',
                s=150,
                marker='*')
    plt.show()
