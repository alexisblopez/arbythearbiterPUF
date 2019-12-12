import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle


def logisticRegression():
    df = pd.read_csv('challenge_response_pairs.csv')
    print(df)

    X = np.array(df.iloc[:, :-1])
    print(X)

    y = np.array(df.iloc[:, -1])
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    linear_regression = LogisticRegression()

    linear_regression.fit(X_train, y_train)
    accuracy = linear_regression.score(X_test, y_test)
    print(accuracy)

    filename = 'finalized_model.sav'
    pickle.dump(linear_regression, open(filename, 'wb'))

    # example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
    # example_measures = example_measures.reshape(len(example_measures), -1)
    # prediction = clf.predict(example_measures)
    # print(prediction)


if __name__ == "__main__":
    logisticRegression()

