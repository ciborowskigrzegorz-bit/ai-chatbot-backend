from fastapi import FastAPI
from backend.routes import chatbot, chatbot_langchain, sentiment

app = FastAPI()

app.include_router(chatbot.router, prefix="/chat")
app.include_router(chatbot_langchain.router, prefix="/chat-langchain")
app.include_router(sentiment.router, prefix="/sentiment")