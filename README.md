# 🤖 AI Chatbot Backend

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Dockerized-yes-blue?logo=docker)
![Tests](https://img.shields.io/badge/tests-pytest-yellow)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-blueviolet)

Projekt backendowy stworzony w FastAPI do obsługi:
- prostego chatbota (`/chat`)
- chatbota z LangChain + GPT-3.5 (`/chat-langchain`)
- analizy sentymentu (`/sentiment`) *(opcjonalnie)*

## 🚀 Uruchamianie

```bash
docker-compose up --build
```

Aplikacja będzie dostępna pod:
```
http://localhost:8000/docs
```

## 🧪 Testowanie

```bash
bash run_tests.sh
```

## 📁 Struktura

```
backend/
├── main.py
├── routes/
│   ├── chatbot.py
│   ├── chatbot_langchain.py
│   └── sentiment.py
tests/
├── test_chatbot.py
├── test_chat_langchain.py
└── test_chat_errors.py
```

## 🧠 Wymagania

- Python 3.11+
- `transformers`, `torch`, `fastapi`, `langchain`, `openai`