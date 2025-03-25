import random
from datetime import datetime

# English responses with Tamil cultural references
responses = {
    "depression": [
        "Even Superstar Rajinikanth had 15 flops before becoming Thalaivar! This is just your 'flop phase' before the blockbuster!",
        "Feeling low like a Chennai summer? Remember - the monsoon always comes eventually!",
        "Depression is like a Kollywood villain - seems powerful now, but the hero always wins in the climax!",
        "Like idli batter needs time to rise, you need patience during low phases. The softness will come!"
    ],
    "anxiety": [
        "Your anxiety is like a Vijay TV serial - 90% unnecessary drama! Let's change the channel!",
        "Remember what we say in Tamil Nadu - 'Adi varum, arugil varum' (Troubles come, solutions follow)!",
        "Anxiety is like a Chennai auto meter - keeps running unnecessarily. Time to say 'Stop!'",
        "Like Bharatanatyam dancers make mistakes but continue beautifully, you'll get through this!"
    ],
    "stress": [
        "Stressed? Do what Madurai people do - grab a tumbler of strong filter coffee and face it!",
        "Office tension? Imagine you're in a Shankar movie - the system will be fixed in the climax!",
        "Exam stress? Remember - even 35/100 is passing marks like in old Madras University!",
        "Stress is like Coimbatore summer - seems unbearable now but the cool breeze will come!"
    ],
    "sleep": [
        "Can't sleep? Try counting Rajini's style moments instead of sheep! Guaranteed sleep in 5 minutes!",
        "Insomnia is like that one relative who keeps talking about 'old Madras days' - let it go and rest!",
        "Remember - even Lord Murugan takes rest during Skanda Shasti. You deserve sleep too!",
        "Sleep tip: Imagine you're listening to Tamil Nadu Assembly debates - fastest lullaby!"
    ],
    "self_care": [
        "Self-care is like sambar - needs daily attention with different ingredients for perfect balance!",
        "Take a break like Nayanthara between movies - even superstars need rest!",
        "Like dosa needs fermentation time, take your 'me-time' seriously for best results!",
        "Pamper yourself like a Kollywood heroine - spa day, temple visit, and good food!"
    ],
    "crisis": [
        "Serious situation! Please call someone immediately - family, friend, or helpline!",
        "Emergency alert! Like Kamal Haasan in 'Vikram', call for backup support now!",
        "This sounds serious! Please reach out to real humans who can help immediately!",
        "Critical situation! Like calling ambulance for roadside bajji overdose, get help fast!"
    ],
    "default": [
        "I'm all ears like a temple elephant during prayers! Tell me more...",
        "Share freely like a Kollywood fan discussing Rajini's latest movie!",
        "Welcome like a Tanjore painting - beautiful and non-judgmental! Speak your heart...",
        "Like the Marina Shore, I'm here to listen to all your waves of thoughts..."
    ]
}

# Tamil cultural keywords to match
keyword_map = {
    "sad": "depression",
    "low": "depression",
    "down": "depression",
    "anxiety": "anxiety",
    "worry": "anxiety",
    "nervous": "anxiety",
    "stress": "stress",
    "pressure": "stress",
    "tension": "stress",
    "sleep": "sleep",
    "insomnia": "sleep",
    "tired": "sleep",
    "care": "self_care",
    "rest": "self_care",
    "exhaust": "self_care",
    "suicide": "crisis",
    "harm": "crisis",
    "emergency": "crisis"
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Crisis check
    if any(key in user_input for key in ["suicide", "kill myself", "end my life"]):
        return random.choice(responses["crisis"])
    
    # Match keywords
    response_category = "default"
    for keyword, category in keyword_map.items():
        if keyword in user_input:
            response_category = category
            break
    
    # Night-time responses
    current_hour = datetime.now().hour
    if current_hour >= 22 or current_hour <= 5:
        if response_category == "default":
            response_category = "sleep"
    
    return random.choice(responses[response_category])

# Example usage
if __name__ == "__main__":
    print("Chatbot: Vanakkam! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Come back like Rajini in 'Baasha'! Take care!")
            break
        print("Chatbot:", get_response(user_input))
