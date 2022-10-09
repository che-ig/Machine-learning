import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

x, y = datasets.make_classification(n_samples=200,
                                    n_classes=3,
                                    n_informative=5)

x_train, x_test, y_train, y_test = train_test_split(x, y)


class KNN:
    def __init__(self, k: int):
        self.k = k
        self.x_train = None
        self.y_train = None

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, test):
        labels = [self.find_label(i) for i in test]
        return labels

    def find_label(self, test):
        distances = [self.distance(i, test) for i in self.x_train]
        k_nears = np.argsort(distances)[:self.k]
        y_labels = [self.y_train[i] for i in k_nears]
        return self.most_common(y_labels)

    def most_common(self, labels):
        unique = np.unique(labels)
        count = [labels.count(i) for i in unique]
        return unique[np.argmax(count)]

    def distance(self, train, test):
        distance = np.sqrt(sum((train - test))**2)
        return distance

    def score(self, predicted, y):
        return np.sum(predicted == y) / len(y)


if __name__ == '__main__':
    test_score = []
    for i in range(2, 11):
        clf = KNN(i)
        clf.fit(x_train, y_train)
        pred = clf.predict(x_test)
        test_score.append(clf.score(pred, y_test))
    plt.plot(test_score)
    plt.ylabel('accuracy')
    plt.xlabel('k')
    plt.show()
    print(test_score)
