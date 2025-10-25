from fastapi import FastAPI
from api.models import PredictRequest, PredictResponse
import inference

app = FastAPI()

transformer, classifier = inference.load_models()


@app.post("/predict")
def make_prediction(request: PredictRequest) -> PredictResponse:
    prediction = inference.predict(request.text, transformer, classifier)
    return PredictResponse(prediction=prediction)
