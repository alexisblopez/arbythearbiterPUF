import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd


def supportVectorMachine():
    df = pd.read_csv('challenge_response_pairs.csv')
    print(df)

    print(df[1:3])

    X = np.array(df.iloc[:, :-1])

    print(X)

    y = np.array(df.iloc[:, -1])
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = svm.SVC()

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(confidence)

    example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
    example_measures = example_measures.reshape(len(example_measures), -1)
    prediction = clf.predict(example_measures)
    print(prediction)


if __name__ == "__main__":
    supportVectorMachine()