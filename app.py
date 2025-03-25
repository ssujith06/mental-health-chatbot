import random
from datetime import datetime

# Enhanced mental health responses
responses = {
    "depression": [
        "It's okay to feel low sometimes. Have you considered talking to a counselor or therapist?",
        "Depression can feel overwhelming, but small steps like going for a walk or talking to a friend can help.",
        "Remember that what you're feeling is valid. Would you like some resources for professional help?",
        "You're not alone in this. Many people find relief through therapy or support groups."
    ],
    "anxiety": [
        "When anxiety strikes, try the 5-4-3-2-1 technique: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, and 1 you taste.",
        "Anxiety often makes us overestimate danger and underestimate our ability to cope. You're stronger than you think.",
        "Progressive muscle relaxation can help - tense and release each muscle group from toes to head.",
        "Would a breathing exercise help right now? Try inhaling for 4 counts, holding for 4, exhaling for 6."
    ],
    "stress": [
        "When stressed, try breaking tasks into smaller steps. What's one small thing you can do right now?",
        "Physical activity, even just stretching, can help reduce stress hormones.",
        "Sometimes writing down what's stressing you can help organize your thoughts.",
        "Remember to take breaks. Even 5 minutes to breathe deeply can reset your system."
    ],
    "sleep": [
        "Good sleep hygiene includes keeping a consistent bedtime and avoiding screens before sleep.",
        "If you can't sleep, try getting up and doing something quiet until you feel sleepy.",
        "A warm drink (without caffeine) and relaxing music might help prepare for sleep.",
        "Worries keeping you up? Try writing them down to address tomorrow."
    ],
    "self_care": [
        "What's something kind you can do for yourself today? Even small acts of self-care matter.",
        "Remember the basics: have you had enough water, food, and rest today?",
        "Sometimes treating yourself like you would a good friend can help shift perspective.",
        "What activity usually helps you feel grounded? Maybe you can make time for that."
    ],
    "crisis": [
        "If you're in immediate distress, please contact a crisis line in your area.",
        "You matter. If you're having thoughts of self-harm, please reach out to a professional now.",
        "National Suicide Prevention Lifeline (US): 988 | International: find a helpline at www.befrienders.org",
        "This sounds serious. Would you like help finding emergency mental health services?"
    ],
    "default": [
        "I'm here to listen. Can you tell me more about what you're experiencing?",
        "That sounds difficult. How long have you been feeling this way?",
        "Thank you for sharing. What would be most helpful to talk about right now?",
        "I hear you. Would you like some suggestions, or just need to talk it out?"
    ]
}

# Additional supportive messages
encouragements = [
    "You're showing real strength by reaching out like this.",
    "Healing isn't linear - it's okay to have difficult days.",
    "Your feelings are valid, even if they're painful right now.",
    "Progress takes time. Be patient with yourself.",
    "Asking for help is a sign of wisdom, not weakness."
]

# Keywords to match
keyword_map = {
    "depress": "depression",
    "sad": "depression",
    "hopeless": "depression",
    "anxio": "anxiety",
    "worry": "anxiety",
    "panic": "anxiety",
    "stress": "stress",
    "overwhelm": "stress",
    "sleep": "sleep",
    "insomnia": "sleep",
    "tired": "sleep",
    "care": "self_care",
    "exhaust": "self_care",
    "suicid": "crisis",
    "harm": "crisis",
    "emergency": "crisis"
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for crisis keywords first
    if any(key in user_input for key in ["suicid", "kill myself", "end it all", "harm myself"]):
        return random.choice(responses["crisis"])
    
    # Check other keywords
    response_category = "default"
    for keyword, category in keyword_map.items():
        if keyword in user_input:
            response_category = category
            break
    
    # Time-sensitive responses
    current_hour = datetime.now().hour
    if current_hour >= 22 or current_hour <= 5:
        if response_category == "default":
            response_category = "sleep"
    
    # Combine category response with occasional encouragement
    if random.random() < 0.3:  # 30% chance to add encouragement
        return f"{random.choice(responses[response_category])} {random.choice(encouragements)}"
    else:
        return random.choice(responses[response_category])

# Example usage
if __name__ == "__main__":
    print("Chatbot: Hello, how are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Take care of yourself. Reach out if you need to talk again.")
            break
        print("Chatbot:", get_response(user_input))
