from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LangChainChatRequest(BaseModel):
    message: str

@router.post("")
def chat_langchain(request: LangChainChatRequest):
    return {"response": f"LangChain odpowiedź na: {request.message}"}