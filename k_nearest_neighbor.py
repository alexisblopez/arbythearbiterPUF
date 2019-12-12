import numpy as np
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier


def kNearestNeighbor():
    df = pd.read_csv('challenge_response_pairs.csv')
    print(df)

    # print("*******")
    # for i in df.columns:
    #     print(i)
    # print(df["0"].value_counts())

    # return
    X = np.array(df.iloc[:, :-1])

    print(X)

    y = np.array(df.iloc[:, -1])
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # calculating best nearest neighbors value
    # params = [{'n_neighbors': [180, 190, 230, 250]}]

    # prev = -10000
    # current_best_param = 10000

    # if prev < current_best_param:
    #     prev = current_best_param

    # knnCV = GridSearchCV(KNeighborsClassifier(), params, cv=3)

    #     current_best_param = knnCV.best_params_

    # knnCV.fit(X_train, y_train)
    # print("Best parameter combo for KNN:")
    # print(knnCV.best_params_)

    clf = neighbors.KNeighborsClassifier(n_neighbors=1000)

    clf.fit(X_train, y_train)

    confidence = clf.score(X_test, y_test)
    print(confidence)

    # y_pred = knnCV.predict(X_test)

    # print(classification_report(y_test, y_pred))
    # print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    # print("Precision [0, 1]:", metrics.precision_score(y_test, y_pred, average=None))
    # print("Recall [0, 1]:", metrics.recall_score(y_test, y_pred, average=None))
    # print("F1 Score [0, 1]: ", metrics.f1_score(y_test, y_pred, average=None))

    filename = 'finalized_model.sav'
    pickle.dump(clf, open(filename, 'wb'))

    # example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
    # example_measures = example_measures.reshape(len(example_measures), -1)
    # prediction = clf.predict(example_measures)
    # print(prediction)


if __name__ == "__main__":
    kNearestNeighbor()
