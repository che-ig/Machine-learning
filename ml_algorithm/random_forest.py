from collections import Counter, namedtuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from numpy.random import beta
from sklearn.datasets import make_classification
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor

Split = namedtuple("Split", ["true_data", "false_data", "true_labels", "false_labels"])
BestSplit = namedtuple("BestSplit", ["best_gain", "best_t", "best_index"])

# сгенерируем данные (500 обьектов с 5 признаками)
classification_data, classification_labels = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=5,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=23,
)

rng = np.random.default_rng(12345)
dots = np.linspace(-10, 10, 100)
x_datas = []
f_datas = []
regressors = []
predictions = []


plt.xlabel("x")
plt.ylabel("f_polynom(x)")
plt.ylim(-5000, 5000)
plt.xlim(-10, 10)


def f_polynom(x):
    return 6 - 13 * x - 5 * x**2 - 4 * x**3


def show_polynom():
    # plt.xlabel("x")
    # plt.ylabel("f_polynom(x)")
    # plt.ylim(-5000, 5000)
    # plt.xlim(-10, 10)

    plt.plot(dots, f_polynom(dots), color="b")
    plt.show()


def create_noisy_data():
    for _ in range(10):
        x_data = rng.uniform(-10, 10, 20)
        x_datas.append(x_data)
        noise = rng.uniform(-500, 500, 20)
        f_datas.append([f_polynom(i) for i in x_data] + noise)


def show_noisy_polynom():
    # plt.xlabel("x")
    # plt.ylabel("noisy_polynom")
    # plt.ylim(-5000, 5000)
    # plt.xlim(-10, 10)

    plt.plot(dots, f_polynom(dots), color="b")
    plt.scatter(x_datas[0], f_datas[0], color="r")
    plt.grid(which="both", axis="both", color="#ccc")
    plt.show()


def show_regression():
    global predictions

    # plt.xlabel("x")
    # plt.ylabel("f_polynom")
    # plt.ylim(-5000, 5000)
    # plt.xlim(-10, 10)

    plt.plot(dots, f_polynom(dots), color="b")
    for i in range(10):
        # создаем модель
        regressor = DecisionTreeRegressor(random_state=10, max_depth=10)
        # обучаем модел
        regressor.fit(x_datas[i].reshape(-1, 1), f_datas[i])
        regressors.append(regressor)

    for i in range(10):
        plt.scatter(x_datas[i], f_datas[i])
        prediction = regressors[i].predict(dots.reshape(-1, 1))
        predictions.append(prediction)
        plt.plot(dots, prediction, color="r")
    predictions = np.array(predictions)
    plt.show()


def show_mean_prediction():
    mean_prediction = predictions.mean(axis=0)
    plt.plot(dots, f_polynom(dots), color="g")
    plt.plot(dots, mean_prediction, color="r")
    plt.show()


def show_skl_data():
    colors = ListedColormap(["red", "blue"])
    plt.figure(figsize=(8, 8))
    # y_idx_max = np.argmax(classification_data[:, 1])
    # y_max = classification_data[y_idx_max][1]
    # x_max = classification_data[y_idx_max][0]
    # plt.scatter(x_max, y_max, c="y", s=300, marker="v")
    plt.scatter(
        classification_data[:, 0],
        classification_data[:, 1],
        c=classification_labels,
        cmap=colors,
    )
    plt.show()


def get_bootstrap(data, labels, N):
    n_samples = data.shape[0]  # размер совпадает с исход. выборкой
    bootstrap = []

    for _ in range(N):
        sample_index = rng.integers(0, n_samples, size=n_samples)
        b_data = data[sample_index]
        b_label = labels[sample_index]

        bootstrap.append((b_data, b_label))

    return bootstrap


# метод случайных подпространств
def get_subsample(len_sample):
    # для задачи классификации оптимальным количеством признаков для обучения
    # является корень из общего количества признаков
    len_subsample = int(np.sqrt(len_sample))
    return rng.choice(len_sample, size=len_subsample, replace=False)


class Node:
    def __init__(self, index, t, true_branch, false_branch):
        # индекс признака, по которому ведется сравнение
        self.index = index
        # пороговое значение
        self.t = t
        # поддерево удовл. условию узла
        self.true_branch = true_branch
        # поддерево не удовл. условию узла
        self.false_branch = false_branch


class Leaf:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.prediction = self.predict()

    def predict(self):
        # получаем класс, который встречается чаще всего в листе
        most_common_label = Counter(self.labels).most_common(1)[0]

        return most_common_label[0]


# Расчет критерия Джини
def gini(labels):
    # подсчет обЬектов разных классов
    uniq = np.unique_counts(labels)
    probability_labels = uniq.counts / np.sum(uniq.counts)

    return 1 - np.sum(np.power(probability_labels, 2))


# Разбиение данных в узле
def split(data, labels, column_index, t):
    left = np.where(data[:, column_index] <= t)
    right = np.where(data[:, column_index] > t)

    true_data = data[left]
    false_data = data[right]

    true_labels = labels[left]
    false_labels = labels[right]

    return Split(true_data, false_data, true_labels, false_labels)


# рассчет прироста
def gain(left_labels, right_labels, root_gini):
    # доля выборки, ушедшая в левое поддерево
    p = float(left_labels.shape[0] / (left_labels.shape[0] + right_labels.shape[0]))
    return root_gini - p * gini(left_labels) - (1 - p) * gini(right_labels)


# Нахождение лучшего разбиения
def find_best_split(data, labels):

    root_gini = gini(labels)

    best_gain = 0
    best_t = Node
    best_index = Node

    n_features = data.shape[1]
    feature_subsample_indices = get_subsample(n_features)  # выбираем случайные признаки

    for index in feature_subsample_indices:
        # будем проверять только уникальные значения признака, исключая повторения
        t_values = np.unique(data[:, index])

        for t in t_values:
            data_true, data_false, true_labels, false_labels = split(
                data, labels, index, t
            )
            current_gain = gain(true_labels, false_labels, root_gini)

            # выбираем порог, на котором получаем максимальный прирост качества
            if current_gain > best_gain:
                best_gain, best_t, best_index = current_gain, t, index

    return BestSplit(best_gain, best_t, best_index)


# построение дерева при помощи рекурсивной функции
def build_tree(data, labels):
    gain, t, index = find_best_split(data, labels)

    # базовый случай - прекращаем рекурсию, когда нет прироста в качестве
    if gain == 0:
        return Leaf(data, labels)

    true_data, false_data, true_labels, false_labels = split(data, labels, index, t)

    # рекурсивно строим 2 поддерева
    true_branch = build_tree(true_data, true_labels)
    false_branch = build_tree(false_data, false_labels)

    # возвращаем класс узла со всеми поддеревьями, т. е целое дерево
    return Node(index, t, true_branch, false_branch)


# формируем случайный лес
def random_forest(data, labels, n_trees):
    forest = []
    bootstrap = get_bootstrap(data, labels, n_trees)

    for b_data, b_labels in bootstrap:
        forest.append(build_tree(b_data, b_labels))

    return forest


# функция классификации отдельного объекта
# obj - это конкретная запись данных (т.е просто строка в датасете)
# node - все дерево решений
def classify_object(obj, node):
    # останавливаем рекурсию, если достигли листа
    if isinstance(node, Leaf):
        return node.prediction

    # каждая нода содержит признак (node.index) и его значение - порога (node.t) при котором
    # происходит лучшее разбиение, поэтому мы у нашей записи смотрим значение именно
    # этот признака
    if obj[node.index] <= node.t:
        return classify_object(obj, node.true_branch)
    else:
        return classify_object(obj, node.false_branch)


# предсказание по выборке на одном дереве
def predict(data, tree):
    classes = []
    for obj in data:
        prediction = classify_object(obj, tree)
        classes.append(prediction)

    return classes


# предсказание голосованием деревьев
def tree_vote(forest, data):
    # добавляем предсказания всех деревьев в список
    predictions = []
    for tree in forest:
        predictions.append(predict(data, tree))

    # формируем список с предсказаниями каждого дерева для конждого объекта индивидуально
    prediction_per_object = list(zip(*predictions))

    # выберем в качестве итогового предсказания для каждого объекта, то за которое
    # проголосовало больше всего деревьев
    voted_predictions = []
    for obj in prediction_per_object:
        voted_predictions.append(max(set(obj), key=obj.count))

    return voted_predictions


# подсчет точности как доля правильных ответов
def accuracy_metric(actual, predicted):
    correct = 0
    len_actual = len(actual)
    for i in range(len_actual):
        if actual[i] == predicted[i]:
            correct += 1

    return correct / float(len_actual) * 100


if __name__ == "__main__":
    n_trees = 20

    train_data, test_data, train_labels, test_labels = train_test_split(
        classification_data, classification_labels, test_size=0.3, random_state=1
    )
    n_trees_1 = random_forest(train_data, train_labels, n_trees)

    # получим ответы на тренировочной выборке
    train_answers = tree_vote(n_trees_1, train_data)

    # получаем ответы на тестовой выборке
    test_answers = tree_vote(n_trees_1, test_data)

    # точность на обучающей выборке
    train_accuracy = accuracy_metric(train_answers, train_labels)
    print(
        f"точность случайного леса из {n_trees} деревьев на обучающей выборке {train_accuracy:.3f}"
    )

    # точность на тестовой выборке
    test_accuracy = accuracy_metric(test_answers, test_labels)
    print(
        f"точность случайного леса из {n_trees} деревьев на тестовой выборке {test_accuracy:.3f}"
    )
    # show_polynom()

    # create_noisy_data()
    # show_noisy_polynom()
    # show_regression()
    # show_mean_prediction()
    # визуализируем сгенерированные данные
    # show_skl_data()
    # print(get_bootstrap(classification_data, classification_labels, 2))
    # print(get_subsample(9))
    # print(get_subsample(4))
