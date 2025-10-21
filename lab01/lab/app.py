from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
import inference

app = FastAPI()
model = inference.load_model(filepath="models/model.joblib")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = inference.predict(request.model_dump(), model)
    return PredictResponse(prediction=prediction)
