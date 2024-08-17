import nltk
import re
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# mapping simple responses to suer inputs
pairs = [
    # Greetings
    [r"hi|hey|hello",
     ["Hello! How can I assist you today?", "Hey there! What can I do for you?", "Hi! How can I help you?"]],
    [r"good morning|good afternoon|good evening", ["Good %1! How can I assist you today?"]],

    # Introductions
    [r"what is your name?", ["I am a chatbot created to assist you. You can call me Chatbot.",
                             "I don't have a personal name, but you can call me Chatbot."]],
    [r"what do you do?", ["I'm here to assist you with various tasks and answer your questions.",
                          "I help answer your questions and provide assistance where I can."]],

    # Asking for Help
    [r"can you help me with (.*)", ["Sure, I can help with %1. Please provide more details.",
                                    "Absolutely, tell me more about %1 and I'll do my best to assist."]],
    [r"i need help with (.*)", ["Of course! What do you need help with regarding %1?",
                                "I'm here to help with %1. What specifically are you looking for?"]],

    # Offering Assistance
    [r"what can you do?", [
        "I can help with answering questions, providing information, and assisting with various tasks. What do you need help with?",
        "I offer assistance with a range of tasks and questions. Just let me know what you need!"]],
    [r"can you (.*)", ["I can certainly try to help with %1. Please provide more details.",
                       "What specifically would you like help with regarding %1?"]],

    # Expressions of Emotion
    [r"how are you?", ["I'm just a bot, so I don't have feelings, but I'm here to help you!",
                       "I don't have feelings, but I'm fully operational and ready to assist you."]],
    [r"i'm feeling (.*)", ["I'm here to listen. Can you tell me more about how you're feeling %1?",
                           "I'm sorry to hear you're feeling %1. How can I assist you today?"]],

    # Apologies and Gratitude
    [r"sorry (.*)", ["It's okay. How can I assist you further?", "No problem. How can I help you?"]],
    [r"thank you|thanks", ["You're welcome!", "No problem at all!", "Glad I could help!"]],

    # Farewells
    [r"bye|goodbye|see you later", ["Goodbye! Have a great day!", "See you later! Have a wonderful day!",
                                    "Bye! If you need anything else, just let me know!"]],
    [r"quit", ["Goodbye! Have a great day!", "See you next time!"]],

    # Small Talk
    [r"what is the weather like?",
     ["I can't check the weather, but you can check a weather website or app for current conditions.",
      "I don't have access to weather information, but you can use a weather app or website for updates."]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!",
                         "What do you call fake spaghetti? An impasta!"]],

    # Clarifications
    [r"(.*) please", ["Certainly! What do you need help with?", "Of course, how can I assist you?"]],
    [r"(.*) sorry", ["No worries! How can I assist you further?", "It's okay. What can I help you with?"]],

    # Miscellaneous
    [r"what time is it?", ["I can't check the time, but you can look at your device's clock for the current time.",
                           "I don't have access to the time, but your device's clock should have the current time."]],
    [r"i don't understand", ["I'm sorry. Could you please clarify or ask something else?",
                             "I apologize if I wasn't clear. Can you provide more details?"]],

    # Default response
    [r"(.*)", ["I'm sorry, I don't understand that. Can you rephrase?",
               "Could you please provide more details or ask something else?"]]
]


class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)


chatbot = RuleBasedChatbot(pairs)

def chat_with_bot():
    print("Hi, Im PAI, your personal artificial intelligence(v 1.0),Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("PAI: Byeee! Have a great day")
            break
        response = chatbot.respond(user_input)

        print(f"PAI: {response}")

chat_with_bot()
