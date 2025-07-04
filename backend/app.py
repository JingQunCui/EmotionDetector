from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer (make sure this path matches your fine-tuned model)
model_name = "distilbert-base-uncased"
num_labels = 6
label_names = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

model = AutoModelForSequenceClassification.from_pretrained("./emotion-model")
tokenizer = AutoTokenizer.from_pretrained("./emotion-model")
model.eval()

app = FastAPI()

class TextIn(BaseModel):
    text: str

@app.post("/predict")
async def predict_emotion(data: TextIn):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return {"emotion": label_names[pred]}
