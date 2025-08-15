
# Simple Rule-Based Chatbot using if-elif-else
# Author: Custom Human-Created Code
# This script demonstrates a basic chatbot interaction in Python.

def chatbot():
    print("Hi! I'm your friendly chatbot. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm feeling chatty!")
        elif "your name" in user_input:
            print("Bot: You can call me PyBot.")
        elif "help" in user_input:
            print("Bot: Sure! I can answer simple questions about me.")
        else:
            print("Bot: Sorry, I didn’t understand that. Could you rephrase?")

if __name__ == "__main__":
    chatbot()
