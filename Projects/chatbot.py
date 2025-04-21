# chatbot.py

import random

# Simple rule-based responses (you can enhance this with an ML model later)
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bunch of code, but thanks for asking!", "Doing great! What about you?"],
    "what is your name": ["I'm your health assistant!", "Call me MediBot."],
    "bye": ["Goodbye!", "Take care!", "See you soon!"],
}

def get_chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that. Could you please rephrase?"
