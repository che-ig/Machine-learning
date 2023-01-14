import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

X, y = datasets.make_classification(n_features=2,
                                    n_informative=2,
                                    n_redundant=0,
                                    n_classes=2,
                                    n_samples=500)

print(X)
