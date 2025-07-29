from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("")
def analyze_sentiment(request: SentimentRequest):
    return {"sentiment": "pozytywny" if "dobrze" in request.text else "neutralny"}