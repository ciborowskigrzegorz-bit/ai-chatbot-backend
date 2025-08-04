from flask import Flask, request, jsonify, session
from flask_session import Session
from openai_client import generate_response
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = "sekret123"  # ważne do działania sesji
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Brak wiadomości."}), 400

    # Inicjalizacja historii
    if "history" not in session:
        session["history"] = []

    # Intencje i entie (opcjonalnie)
    intent = detect_intent(user_message)
    entities = extract_entities(user_message)

    if "name" in entities:
        session["username"] = entities["name"]

    # Zapisz wiadomość użytkownika
    session["history"].append({"role": "user", "content": user_message})
    session["history"] = session["history"][-10:]  # ogranicz długość

    # Stwórz kontekst
    context = session["history"]

    # Generowanie odpowiedzi
    if intent == "ask_name":
        response = f"Twoje imię to {session.get('username', 'nieznane')}."
    elif intent == "tell_joke":
        response = "Dlaczego Java nie może pić kawy? Bo jest już zaprogramowana."
    else:
        response = generate_response(user_message, context=context)

    # Zapisz odpowiedź
    session["history"].append({"role": "bot", "content": response})
    session["history"] = session["history"][-10:]

    return jsonify({
        "response": response,
        "context": session["history"],
        "username": session.get("username", None)
    })
