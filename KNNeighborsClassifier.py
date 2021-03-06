import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

INPUT_PATH = r'C:\Users\eviatar\OneDrive\Documents\Python Venv\FitImage\vector_to_predict'
DATA_PATH = r'C:\Users\eviatar\OneDrive\Documents\Python Venv\FitImage\TrainData'


def split_data(df):
    y = df.iloc[:, 0]
    x = df.iloc[:, 1:]
    return x.to_numpy(), y.to_numpy()


def main():
    df = pd.read_csv(DATA_PATH)
    x, y = split_data(df)
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(x, y)
    v = pd.read_csv(INPUT_PATH, squeeze=True).iloc[:, 1:].to_numpy()

    # todo: check why transpose were needed
    prediction = classifier.predict(v.T)
    print(prediction)


if __name__ == '__main__':
    main()
