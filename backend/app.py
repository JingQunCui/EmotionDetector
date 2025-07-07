from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app = FastAPI()

# Load environment variables from .env
load_dotenv()

# Get the allowed origins from the .env
raw_origins = os.getenv("ALLOWED_ORIGINS", "")
origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

# Allow your frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextIn(BaseModel):
    text: str

@app.post("/predict")
async def predict_emotion(data: TextIn):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return {"emotion": label_names[pred]}
