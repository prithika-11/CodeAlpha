import nltk
nltk.download('punkt')
import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

# Example pairs for simple conversation
pairs = [
    [
        r"(hi|hello|hey|holla|hola)",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No worries!", "Don't worry about it."]
    ],
    [
        r"(.) (help|support|assist) (.)",
        ["Sure, I'm here to help. What do you need assistance with?"]
    ],
    [
        r"what is your name ?",
        ["I'm a simple chatbot.", "You can call me ChatBot."]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by a Python developer using NLTK."]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "See you later!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["Tell me more.", "Interesting.", "Let's talk about something else.", "I'm listening."]
    ]
]

def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
