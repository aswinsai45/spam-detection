from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load model & vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# FastAPI app
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] if you want stricter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define input format
class Message(BaseModel):
    message: str

@app.post("/predict")
def predict(data: Message):
    text = data.message
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return {"prediction": prediction}
# To run the app, use the command:
# uvicorn app:app --reload