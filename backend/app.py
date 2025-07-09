from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
from routes import auth
from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM
from utils.emotion_model import predict_emotion
import torch
import os

# Load environment variables from .env
load_dotenv()

# Get the allowed origins from the .env
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI()

app.include_router(auth.router)

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

oauth2_scheme = OAuth2PasswordBearer(tokenURL='login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.options("/predict")
async def options_handler(request: Request):
    return JSONResponse(status_code=200, content={"message": "Preflight OK"})

@app.post("/predict")
async def predict_emotion(data: TextIn, user: str = Depends(get_current_user)):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = outputs.logits.argmax(dim=1).item()
    return {"emotion": label_names[pred]}
