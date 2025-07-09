from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
import torch
import os

# Load model and tokenizer (make sure this path matches your fine-tuned model)
model_name = "distilbert-base-uncased"
num_labels = 6
label_names = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

model = AutoModelForSequenceClassification.from_pretrained("./emotion-model")
tokenizer = AutoTokenizer.from_pretrained("./emotion-model")
model.eval()

# Load environment variables from .env
load_dotenv()

# Get the allowed origins from the .env
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI()

# Allow your frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins],  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextIn(BaseModel):
    text: str

@app.options("/predict")
async def options_handler(request: Request):
    return JSONResponse(status_code=200, content={"message": "Preflight OK"})

@app.post("/predict")
async def predict_emotion(data: TextIn):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return {"emotion": label_names[pred]}
