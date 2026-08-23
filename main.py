from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Deployment!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict():
    return {
        "prediction": "approved",
        "confidence": 0.92
    }