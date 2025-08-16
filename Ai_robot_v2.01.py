import datetime
import random
import time
import json
import os

name = input("Enter your name: ").lower()

# Memory file setup
memory_file = "memory.json"
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump({"notes": []}, f)

# Load memory
with open(memory_file, "r") as f:
    memory = json.load(f)

def save_memory():
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=4)

def tell_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def tell_joke():
    jokes = [
        "Robot ne chai kyun banayi? Kyunki chutiya to nahi bana sakta tha! 🤖",
        "Main AI hoon, mere jokes bhi algorithm se chalte hain. 😆",
        "Mujhe ek error mila... par maine usse friend bana liya! 💻"
    ]
    return random.choice(jokes)

def calculator():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    c = input("Press (a) add, (s) subtract, (d) divide, (m) multiply: ").lower()

    if c == "a":
        print("Sum:", num1 + num2)
    elif c == "s":
        print("Difference:", num1 - num2)
    elif c == "d":
        if num2 == 0:
            print("❌ Cannot divide by zero!")
        else:
            print("Division:", num1 / num2)
    elif c == "m":
        print("Multiply:", num1 * num2)
    else:
        print("Invalid operation.")

def time_greeting():
    hour = time.localtime().tm_hour
    if hour < 12:
        print(f"🌅 Good morning {name}")
    elif hour < 16:
        print(f"🌞 Good afternoon {name}")
    elif hour < 20:
        print(f"🌆 Good evening {name}")
    else:
        print(f"🌙 {name}, raat ho gai hai par hum abhi continue karenge!")

# MAIN LOOP
while True:
    command = input("\n👉 Command do: ").lower()

    if command == "time":
        print("⏰ Current Time:", tell_time())

    elif command == "joke":
        print("😂 Joke:", tell_joke())

    elif "calculate" in command:
        calculator()

    elif "remember" in command:
        thing = input("Kya yaad rakhna hai? ")
        memory["notes"].append(thing)
        save_memory()
        print("👍 Ok, maine yaad rakh liya!")

    elif "recall" in command:
        if memory["notes"]:
            print("📖 Tumne mujhe ye yaad karaya hai:")
            for i, note in enumerate(memory["notes"], start=1):
                print(f"{i}. {note}")
        else:
            print("Mere paas abhi koi memory nahi hai.")

    elif "search" in command:
        word = input("Kya search karna hai memory me? ").lower()
        found = [note for note in memory["notes"] if word in note.lower()]
        if found:
            print("🔎 Search Results:")
            for i, note in enumerate(found, start=1):
                print(f"{i}. {note}")
        else:
            print("❌ Memory me kuch nahi mila.")

    elif "forget" in command:
        if memory["notes"]:
            print("Kaun si memory delete karni hai?")
            for i, note in enumerate(memory["notes"], start=1):
                print(f"{i}. {note}")
            try:
                idx = int(input("Index number do: ")) - 1
                if 0 <= idx < len(memory["notes"]):
                    removed = memory["notes"].pop(idx)
                    save_memory()
                    print(f"🗑 Memory delete ho gayi: {removed}")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Invalid input.")
        else:
            print("Koi memory nahi hai delete karne ke liye.")

    elif "exit" in command:
        print(f"👋 Good night {name}, bye!")
        break

    else:
        print("❓ Mujhe ye command nahi aati.")