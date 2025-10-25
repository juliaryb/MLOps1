from sentence_transformers import SentenceTransformer
import joblib

SENTIMENT_LABELS = {0: "negative", 1: "neutral", 2: "positive"}  # hardcoded class names


def load_models(
    transformer_path="models/sentence_transformer.model",
    classifier_path="models/classifier.joblib",
):
    transformer = SentenceTransformer(transformer_path)
    classifier = joblib.load(classifier_path)

    return transformer, classifier


def predict(text_input: str, transformer, classifier) -> str:
    """
    Performs sentiment analysis by:
    1. Embedding the input text using the specified Sentence Transformer.
    2. Classifying the embedding into one of 3 classes (0 (negative), 1 (neutral), or 2 (positive)) using logistic regression.
    """

    embedding = transformer.encode(text_input, convert_to_numpy=True)
    embedding_2d = embedding.reshape(1, -1)
    predicted_class_num = classifier.predict(embedding_2d)[0]

    return SENTIMENT_LABELS[predicted_class_num]
