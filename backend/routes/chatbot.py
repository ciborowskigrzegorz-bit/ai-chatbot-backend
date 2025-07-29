from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("")
def chat(request: ChatRequest):
    return {"response": f"Odpowiedź na: {request.message}"}