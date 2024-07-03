from enum import Enum

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import Ridge as Ridge_skl
from sklearn.model_selection import train_test_split

X, y = datasets.make_regression(n_samples=500)
X_train, X_test, y_train, y_test = train_test_split(X, y)


class GD(Enum):
    FULL = "full"
    STOCHASTIC = "stochastic"
    MINI_BATCH = "mini_batch"


class LenearRegression:
    def __init__(self, lr=0.05, tolerance=0.01):
        self.lr = lr
        self.tolerance = tolerance
        self.weights = []
        self.score = []

    def fit(self, X, y, gd=GD.FULL):
        np.random.seed(28)

        if gd == GD.FULL:
            self._fit_gd_full(X, y)
        elif gd == GD.MINI_BATCH:
            self._fit_mini_batch(X, y)

    def predict(self, X):
        X = self.add_ones_feature(X)
        return X.dot(self.weights)

    def add_ones_feature(self, X):
        return np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

    def r2(self, predict, y):
        return 1 - np.sum((predict - y) ** 2) / np.sum((y.mean() - y) ** 2)

    def _fit_gd_full(self, X, y):
        X = self.add_ones_feature(X)
        n_samples, n_features = X.shape
        self.weights = np.random.rand(n_features) * 0.1

        learnign = True
        while learnign:
            predict = X.dot(self.weights)
            error = predict - y
            dw = 2 / n_samples * X.T.dot(error)
            self.weights -= self.lr * dw
            self.score.append(self.r2(predict, y))

            # Условие остановки обучения
            if (
                len(self.score) > n_features
                and self.score[-1] - self.score[-n_features] < self.tolerance
            ):
                learnign = False

    def _fit_mini_batch(self, X, y):
        X = self.add_ones_feature(X)
        n_samples, n_features = X.shape
        self.weights = np.random.rand(n_features) * 0.1

        learnign = True
        predict = X.dot(self.weights)
        while learnign:
            indexes = np.random.choice(n_samples, int(n_samples * 0.01), replace=False)
            predict_batch = X[indexes].dot(self.weights)
            error = predict_batch - y[indexes]
            dw = 2 / n_samples * X[indexes].T.dot(error)
            self.weights -= self.lr * dw
            predict[indexes] = predict_batch
            self.score.append(self.r2(predict, y))

            # Условие остановки обучения
            if (
                len(self.score) > n_features
                and self.score[-1] - self.score[-n_features] < self.tolerance
            ):
                learnign = False


def full_gd():
    for i in [0.1, 0.05, 0.01]:
        reg = LenearRegression(lr=i)
        reg.fit(X_train, y_train)
        plt.plot(reg.score, label=f"learning rate {i}")

        predict = reg.predict(X_test)
        print(f"r2 при learning rate = {i}", reg.r2(predict, y_test))

    plt.title("The full GD")
    plt.legend()
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.show()


def mini_batch_gd():
    for i in [0.1, 0.05, 0.01]:
        reg = LenearRegression(lr=i)
        reg.fit(X_train, y_train, gd=GD.MINI_BATCH)
        plt.plot(reg.score, label=f"learning rate {i}")

        predict = reg.predict(X_test)
        print(f"r2 при learning rate = {i}", reg.r2(predict, y_test))

    plt.title("The mini batch GD")
    plt.legend()
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.show()


if __name__ == "__main__":
    full_gd()
    mini_batch_gd()
