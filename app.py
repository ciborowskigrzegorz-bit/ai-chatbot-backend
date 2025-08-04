import openai
import gradio as gr
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

history = []

def chat(user_input):
    history.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    message = response.choices[0].message["content"]
    history.append({"role": "assistant", "content": message})
    return message

iface = gr.Interface(fn=chat, inputs="text", outputs="text", title="Chatbot GPT")
iface.launch()
