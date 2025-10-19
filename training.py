import os
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    X, y = load_iris(return_X_y=True)
    print(X[0])
    return X, y


def train_model(X, y):
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model, filepath="models/model.joblib"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")


if __name__ == "__main__":
    features, target = load_data()
    trained_model = train_model(features, target)
    save_model(trained_model, "models/model.joblib")
