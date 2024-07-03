from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge as Ridge_skl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

np.random.seed(34)

Data = namedtuple("Data", ["X", "y"])
SplitedData = namedtuple("SplitedData", ["X_train", "y_train", "X_test", "y_test"])
Errors = namedtuple("Errors", ["mse", "r"])


class Ridge:
    def __init__(
        self, reg_coef, lr=0.1, epoch=200, log_interval=200, print_log_loss=None
    ):
        self.lr = lr
        self.epoch = epoch
        self.weights = []
        self.X_train = []
        self.y_train = []
        self.score = []
        self.reg_coef = reg_coef
        self.log_interval = log_interval
        self.print_log_loss = print_log_loss

    def add_ones_feature(self, X):
        return np.hstack((np.ones((X.shape[0], 1)), X))

    def loss(self, X, y):
        mse = np.square(X.dot(self.weights) - y).mean()
        r = self.reg_coef * self.weights.T.dot(self.weights)
        return Errors(mse, round(r.flat[0], 9))

    def fit(self, X_train, y_train):
        self.X_train = self.add_ones_feature(X_train)
        self.y_train = y_train.reshape(-1, 1)

        n_samples, n_features = self.X_train.shape
        self.weights = np.zeros((n_features, 1))

        for epoch in range(self.epoch):
            predict = self.X_train.dot(self.weights)
            error = predict - self.y_train
            dMSEdw = 2 / n_samples * self.X_train.T.dot(error)
            dRdw = 2 * self.reg_coef * self.weights

            if epoch % self.log_interval == 0 and self.print_log_loss:
                self.print_loss(self.X_train, self.y_train)

            self.weights -= self.lr * (dMSEdw + dRdw)

        if self.print_log_loss:
            self.print_loss(self.X_train, self.y_train)

    def print_loss(self, X, y):
        mse, r = self.loss(X, y)
        print(f"MSE: {round(mse, 9)}")
        print(f"loss: {mse + r}")
        print("-" * 25)


def generate_data_for_ridge(n=300):
    deg_from = -130
    deg_to = 130

    X = np.linspace(deg_from, deg_to, n) * np.pi / 180
    y = np.sin(X)

    return Data(X, y)


def get_splited_data(data):
    np.random.seed(34)
    X, y = data.X, data.y
    n_samples = len(X)
    n_train = int(0.8 * n_samples)
    y = y + np.random.randn(n_samples) * 0.2

    perm = np.random.permutation(n_samples)
    train_idxs = np.sort(perm[:n_train])
    test_idxs = np.sort(perm[n_train:])

    X_train, y_train = X[train_idxs], y[train_idxs]
    X_test, y_test = X[test_idxs], y[test_idxs]
    return SplitedData(X_train, y_train, X_test, y_test)


def visualisation_data(data, splited_data):
    plt.plot(data.X, data.y)
    plt.scatter(splited_data.X_train, splited_data.y_train, c="r", label="train")
    plt.scatter(splited_data.X_test, splited_data.y_test, c="g", label="test")
    plt.show()


def get_complexity_data(data):
    polynom_degree = 15
    data_deg = np.array([data**deg for deg in range(1, polynom_degree + 1)])
    return data_deg.T


def get_normalized_data(data):
    scalar = StandardScaler()
    return scalar.fit_transform(data)


def get_min_max_scaler_data(data):
    scalar = MinMaxScaler()
    return scalar.fit_transform(data)


def work_for_ridge():
    data = generate_data_for_ridge(300)
    splited_data = get_splited_data(data)
    x_train_data_complex = get_complexity_data(splited_data.X_train)
    x_test_data_complex = get_complexity_data(splited_data.X_test)

    x_train_std = get_min_max_scaler_data(x_train_data_complex)
    x_test_std = get_min_max_scaler_data(x_test_data_complex)
    # x_train_std = get_normalized_data(x_train_data_complex)
    # x_test_std = get_normalized_data(x_test_data_complex)
    visualisation_data(data, splited_data)

    scores_train = []
    scores_test = []

    # Работа с оригинальным классом Ridge
    #  alpha_range = range(1, 2)
    #  for a in alpha_range:
    #      ridge = Ridge_skl(alpha=a)
    #      f = ridge.fit(x_train_data_complex, splited_data.y_train)
    #      # c = ridge.predict(x_test_data_complex)
    #      scores_train.append(
    #          ridge.score(x_train_data_complex, splited_data.y_train))
    #      scores_test.append(
    #          ridge.score(x_test_data_complex, splited_data.y_test))
    #      # print(f'score_train: {score_train}')
    #      # print(f'score_test: {score_test}')
    #  print(f)
    #  plt.title('The Ridge regression')
    #  plt.plot(alpha_range, scores_train, c='g', label='Train')
    #  plt.plot(alpha_range, scores_test, c='r', label='Test')
    #  plt.legend()
    #  plt.show()

    range_r = np.linspace(0, 5, 100)
    for r in range_r:
        model = Ridge(epoch=300, reg_coef=r, log_interval=20)
        x_test_std_added_clm = model.add_ones_feature(x_test_std)
        x_train_std_added_clm = model.add_ones_feature(x_train_std)
        model.fit(x_train_std, splited_data.y_train)

        mse_train, r_train = model.loss(model.X_train, splited_data.y_train)
        mse_test, r_test = model.loss(x_test_std_added_clm, splited_data.y_test)

        scores_train.append(mse_train + r_train)
        scores_test.append(mse_test + r_test)
        print(f"r: {r}")
        model.print_loss(model.X_train, splited_data.y_train.reshape(-1, 1))

    plt.plot(range_r, scores_train, c="g", label="Train")
    plt.plot(range_r, scores_test, c="r", label="Test")
    plt.xlabel("r")
    plt.ylabel("mse")
    plt.legend()
    plt.show()

    # model = Ridge(epoch=300,
    #               reg_coef=3.05,
    #               log_interval=20,
    #               print_log_loss=True)
    # model.fit(x_train_std, splited_data.y_train)
    # print(f'norm_2: {np.linalg.norm(model.weights, 2)}')
    # model.print_loss(model.X_train, splited_data.y_train.reshape(-1, 1))


if __name__ == "__main__":
    work_for_ridge()
