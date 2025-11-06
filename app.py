from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("model.pkl")

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisInput):
    X = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    result = model.predict(X)[0]
    return {"predicted_class": int(result)}
