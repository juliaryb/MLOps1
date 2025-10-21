from fastapi import FastAPI
from api.models import PredictRequest, PredictResponse

app = FastAPI()

@app.post("/predict")
def make_prediction(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction="positive")