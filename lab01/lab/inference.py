import joblib
import numpy as np

IRIS_CLASS_NAMES = ["setosa", "versicolor", "virginica"]  # hardcoded from documentation


def load_model(filepath="models/model.joblib"):
    model = joblib.load(filepath)
    print(f"Loaded model from {filepath}")
    return model


def predict(data: dict, model) -> str:
    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    ]

    predicted_class_num = model.predict(np.array(features).reshape(1, -1))[0]

    return IRIS_CLASS_NAMES[predicted_class_num]


if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully.")

    sample_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    print(f"Making prediction for sample: {sample_data}")

    prediction = predict(sample_data, model)

    print(f"Predicted class: {prediction}")
