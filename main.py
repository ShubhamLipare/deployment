import os

from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")


@app.get("/")
def home():
    return {
        "message": "Hello Deployment!",
        "environment": APP_ENV
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict():
    return {
        "prediction": "approved",
        "confidence": 0.92
    }