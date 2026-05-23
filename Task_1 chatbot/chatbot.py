from colorama import Fore, init
import time
import random
from datetime import datetime

# Start colorama
init()
motivations = [
    "Push yourself, because no one else will do it for you.",
    "Small progress is still progress.",
    "Dream big and dare to fail.",
    "Success starts with self-discipline.",
    "Believe in yourself and keep learning."
]

# Typing effect function
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# Welcome Screen
print(Fore.CYAN + "=" * 50)
typing_effect("🤖 Welcome to CampusBuddy - Student Helper Chatbot")
print(Fore.CYAN + "=" * 50)

# User name
name = input(Fore.YELLOW + "\nEnter your name: ")
typing_effect(Fore.GREEN + f"\nHello {name}! 😊")
typing_effect("I am your Student Helper Chatbot.")

typing_effect(Fore.CYAN + """
I can help you with:
✔ Greetings
✔ Motivation
✔ Study Tips
✔ Attendance
✔ Time & Date
✔ Python & DSA
✔ Jokes
""")

typing_effect("Type 'bye' anytime to exit.\n")
while True:

    user = input(Fore.YELLOW + f"\n{name}: ").lower()

# Greeting
    if user in ["hello", "hi", "hey"]:
        typing_effect(Fore.GREEN + "Hello! How can I help you today? 😊")

# How are you
    elif "how are you" in user:
        typing_effect(Fore.GREEN + "I'm doing great! Thanks for asking 💙")

# Mood Detection
    elif "sad" in user or "stressed" in user or "tired" in user:
        typing_effect(Fore.MAGENTA + "Don't worry 😊")
        typing_effect("Take a deep breath and focus on one step at a time.")
        typing_effect("You are stronger than your stress 💪")

# Motivation
    elif "motivate" in user:
        typing_effect(Fore.CYAN + "🔥 Motivation Boost:")
        typing_effect(random.choice(motivations))

# Joke Feature
    elif "joke" in user:
        typing_effect(Fore.BLUE + "😂 Why do programmers hate nature?")
        typing_effect("Because it has too many bugs!")

# Study Tips
    elif "study" in user:
        typing_effect(Fore.GREEN + "📚 Study Tips:")
        typing_effect("1. Study for 50 minutes")
        typing_effect("2. Take a 10 minute break")
        typing_effect("3. Revise before sleeping")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        typing_effect(Fore.CYAN + f"⏰ Current time is: {current_time}")
# Date Feature
    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        typing_effect(Fore.CYAN + f"📅 Today's date is: {current_date}")
    
# Programming Help
    elif "python" in user:
        typing_effect(Fore.GREEN + "🐍 Python is beginner-friendly and powerful.")
        typing_effect("It is widely used in AI, Web Development, and Automation.")

    elif "dsa" in user:
        typing_effect(Fore.GREEN + "📘 DSA improves problem-solving skills.")
        typing_effect("Practice arrays, strings, and sorting daily.")
    
# Attendance Calculator
    elif "attendance" in user:

        total = int(input("Enter total classes: "))
        attended = int(input("Enter attended classes: "))
        percentage = (attended / total) * 100

        typing_effect(Fore.CYAN + f"📊 Your attendance is {percentage:.2f}%")

        if percentage >= 75:
            typing_effect(Fore.GREEN + "✅ Good! You are safe.")
        else:
            typing_effect(Fore.RED + "⚠️ Warning! Attendance below 75%")

# Bye
    elif user == "bye":
        typing_effect(Fore.RED + "Goodbye! Study well and stay confident 🚀")
        break

# Unknown response
    else:
        typing_effect(Fore.RED + "Sorry, I don't understand that yet.")




        