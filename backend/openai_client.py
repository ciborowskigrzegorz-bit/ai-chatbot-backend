import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_message, context=None):
    messages = []

    if context:
        messages.extend(context)
    else:
        messages.append({"role": "system", "content": "Jesteś pomocnym asystentem."})

    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # lub "gpt-3.5-turbo"
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"[Błąd generowania odpowiedzi: {e}]"
