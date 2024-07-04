from __future__ import annotations

from typing import List

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# from _annfrom _an
X, y = datasets.make_classification(
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_classes=4,
    n_samples=500,
    n_clusters_per_class=1,  # кол. кластеров в классе
)

X_train, X_test, y_train, y_test = train_test_split(X, y)


class SoftMaxRegression:
    """Класс мультиклассовой регрессии."""

    def __init__(self: SoftMaxRegression) -> None:
        """Конструктор класса."""
        self.classes = None
        self.weights = None
        self.log_loss = [float]
        self.train_score = [float]
        self.learning_rate = 0.1
        self.era = 250

    @staticmethod
    def add_ones_column(X):
        """Добавляем к данным столбец с единицами."""
        """Делаем это, чтобы избавить себя от нахождения лишней производной
        по по смещения (в матрицу весов тоже будет добавлен доп. столбец)"""

        return np.hstack((np.ones((X.shape[0], 1)), X))

    @staticmethod
    def soft_max(sum_k: List[float]) -> List[float]:
        """
        Преобразует входной вектор в вектор вероятностей.

        Для преобразования входного вектора в вектор вероятностей используется
        функция softmax.
        """
        # Рекомендуется из набора данных вычесть макс. зн.
        # для устойчивости решения.
        modif_sum_k = sum_k - np.max(sum_k)
        softmax = np.exp(modif_sum_k) / np.sum(np.exp(modif_sum_k), axis=1).reshape(-1, 1)
        return softmax

    def fit(self: SoftMaxRegression, X, y) -> None:
        """Обучаем модель."""
        self.classes = len(np.unique(y))

        # Сначала добавляем к обучающим данным столбец с единицами, чтобы
        # не возиться со свободным членом.
        modif_X = self.add_ones_column(X)

        self.weights = np.ones((modif_X.shape[1], self.classes))

        for _ in range(self.era):
            sum_k = np.dot(modif_X, self.weights)
            prob_k = self.soft_max(sum_k)
            y_k = np.zeros((modif_X.shape[0], self.classes))

            # Закодируем наши целевые метки при помощи onehotencoder
            # TODO: На данный момент не очень понятен механизм
            # заполнения столбцов.
            y_k[np.arange(len(y)), y] = 1
            dw = 1 / len(y) * modif_X.T.dot(prob_k - y_k)
            self.weights -= dw * self.learning_rate

            # Это функция издержек перекрестной энтропии.
            self.log_loss.append(-np.mean(np.log(prob_k[np.arange(len(y)), y])))
            # Вычисляем score на каждой итерации обучения.
            self.train_score.append(self.score(self.predict(X), y))

    def predict(self: SoftMaxRegression, X):
        """
        Возвращаем метки класса.

        Которые имеют мак. вероятность соответствия текущим данным.
        """
        modif_X = self.add_ones_column(X)
        sum_k = np.dot(modif_X, self.weights)
        prob_k = self.soft_max(sum_k)
        return np.argmax(prob_k, axis=1)

    def score(self: SoftMaxRegression, predicted, y) -> float:
        """Текущий уровень обученности модели."""
        return np.sum(predicted == y) / len(y)


def show_graph(log_loss, train_score) -> None:
    plt.plot(log_loss, label="log_loss")
    plt.plot(train_score, label="train_score")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sm = SoftMaxRegression()
    sm.fit(X_train, y_train)
    predict = sm.predict(X_test)

    show_graph(sm.log_loss, sm.train_score)
    print(sm.score(predict, y_test))
