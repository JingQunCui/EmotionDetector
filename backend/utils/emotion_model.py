from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

label_names = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
tokenizer = AutoTokenizer.from_pretrained("./emotion-model")
model = AutoModelForSequenceClassification.from_pretrained("./emotion-model")
model.eval()

def predict_emotion(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return label_names[pred]
