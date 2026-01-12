from fastapi import FastAPI
from api.models import PredictRequest, PredictResponse
import inference

app = FastAPI()

transformer, classifier = inference.load_models()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def make_prediction(request: PredictRequest) -> PredictResponse:
    prediction = inference.predict(request.text, transformer, classifier)
    return PredictResponse(prediction=prediction)
