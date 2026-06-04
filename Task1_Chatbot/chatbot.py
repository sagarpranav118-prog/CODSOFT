# Rule-Based Chatbot
# Created by Pranav Sagar
# CodSoft AI Internship - Task 1

print("=" * 50)
print("      WELCOME TO CODBOT CHATBOT")
print("=" * 50)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ").lower().strip()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you" or user == "how are you?":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "who are you" or user == "who are you?":
        print("Bot: I am a Chatbot.")

    elif user == "are you interesting" or user == "are you interesting?":
        print("Bot: may be! if you found me so.")

    elif user == "what is your name" or user == "what is your name?":
        print("Bot: My name is CodBot.")

    elif user == "who made you" or user == "who made you?":
        print("Bot: I was created by Pranav Sagar for the CodSoft AI Internship.")

    elif user == "what can you do" or user == "what can you do?":
        print("Bot: I can answer basic predefined questions and assist with simple conversations.")


    elif user == "thanks" or user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("\nBot: Available commands:")
        print(" - hi")
        print(" - hello")
        print(" - how are you")
        print(" - who are you")
        print(" - are you interesting")
        print(" - what is your name")
        print(" - who made you")
        print(" - what can you do")
        print(" - thanks")
        print(" - help")
        print(" - bye\n")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")
        print("Bot: Type 'help' to see available commands.")
