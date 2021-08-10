import numpy as np
import sklearn
from sklearn import datasets
from sklearn import model_selection

class Distance:
    def __init__(self, d, label):
        self.d = d
        self.label = label
    def __str__(self):
        return str(self.label)
    def __repr__(self):
        return self.d
    def __lt__(self, other):
        return self.d < other.d
    def __gt__(self, other):
        return self.d > other.d

class LabelCount:
    def __init__(self, label):
        self.count = 1
        self.label = label
    def __repr__(self):
        return self.count
    def inc(self):
        self.count += 1
    def __str__(self):
        return self.label
    def __lt__(self, other):
        return self.count < other.count

class LabelsCount:
    def __init__(self):
        self.labels = []
        self.labels_names = {}
    def put(self, name):
        if name in self.labels_names:
            self.labels[self.labels_names[name]].inc()
        else:
            self.labels_names[name] = len(self.labels)
            self.labels.append(LabelCount(name))
    def vote(self):
        return str(sorted(self.labels)[0])


class KNNClassifier:
    def __init__(self):
        pass
    def fit(self, X, y):
        self.X = X
        self.y = y
    def predict(self, data):
        dists = []
        for index, x in enumerate(self.X):
            dists.append(Distance(np.linalg.norm(x-data), self.y[index]))
        knn = sorted(dists)[:3]
        return int(self.knn_vote(knn))
    def knn_vote(self, knn):
        labels = LabelsCount()
        for label in knn:
            labels.put(str(label))
        return labels.vote()


if __name__ == '__main__':
    X,y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)
    knn_classifier = KNNClassifier()
    knn_classifier.fit(X_train, y_train)
    for index, value in enumerate(X_test):
        print(knn_classifier.predict(value) == y_test[index])
