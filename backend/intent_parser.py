def detect_intent(message):
    message = message.lower()
    if "nazywam się" in message:
        return "introduce"
    elif "jak się nazywam" in message:
        return "ask_name"
    elif "żart" in message:
        return "tell_joke"
    return "chat"

def extract_entities(message):
    if "nazywam się" in message:
        name = message.split("nazywam się")[-1].strip().split()[0]
        return {"name": name.capitalize()}
    return {}
