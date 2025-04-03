# Simple mental health chatbot responses
responses = {
    "depression": [
        "It's okay to feel this way. Have you considered talking to someone?",
        "You're not alone in this. Many people find help through counseling."
    ],
    "anxiety": [
        "Try taking slow, deep breaths. Inhale for 4 seconds, hold for 4, exhale for 4.",
        "Anxiety can feel overwhelming, but it's manageable with support."
    ],
    "default": [
        "I'm here to listen. Can you tell me more?",
        "That sounds difficult. How can I help?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()
    if "depress" in user_input:
        return responses["depression"][0]
    elif "anxiet" in user_input:
        return responses["anxiety"][0]
    else:
        return responses["default"][0]