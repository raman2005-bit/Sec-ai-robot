import random

# ---------------------------
#  USER SETUP
# ---------------------------
name = input("Enter your name: ").strip().lower()
age = int(input("Enter your age: "))
robot = input("Enter robot name: ").strip().lower()
battery_level = int(input("Enter battery level (0-100): "))

# ---------------------------
#  MOOD DETECTION
# ---------------------------
happy_words = ["happy", "good", "awesome", "mast", "great", "khush"]
sad_words = ["sad", "bad", "bura", "dukhi", "down"]
angry_words = ["angry", "gussa", "mad", "irritated"]

def detect_mood(message):
    message = message.lower()
    if any(word in message for word in happy_words):
        return "happy"
    elif any(word in message for word in sad_words):
        return "sad"
    elif any(word in message for word in angry_words):
        return "angry"
    else:
        return "neutral"

# ---------------------------
#  BATTERY CHECK
# ---------------------------
def battery_check():
    global battery_level
    if battery_level < 20:
        print("⚠ Battery low! Please recharge soon.")
    elif battery_level < 50:
        print("🔋 Battery is okay, but keep an eye.")
    else:
        print("✅ Battery level is good.")
    return battery_level

# ---------------------------
#  BATTERY RECHARGE (NEW FEATURE 1)
# ---------------------------
def recharge():
    global battery_level
    add = int(input("Battery ko kitna recharge karoon (0-100): "))
    battery_level += add
    if battery_level > 100:
        battery_level = 100
    print(f"🔌 Battery recharged! Current level: {battery_level}%")
    battery_check()

# ---------------------------
#  ROBOT DECISION LOGIC
# ---------------------------
sensor_data = [
    "Obstacle detected", "Path clear", "Low light", "Human detected",
]

def robot_decision(sensor_input):
    decisions = {
        "Obstacle detected": "Turning right to avoid collision",
        "Path clear": "Moving forward",
        "Low light": "Turning on headlights",
        "Human detected": "Saying: Hello, human!",
    }
    return decisions.get(sensor_input, "Standing by")

# ---------------------------
#  CHAT MODE + SAVE LOG (NEW FEATURE 2)
# ---------------------------
def save_chat_log(user_msg, bot_msg):
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user_msg}\nRobot: {bot_msg}\n---\n")

def chat():
    global battery_level
    print("\n💬 Chat mode started! Type 'bye' to exit chat.\n")
    while True:
        u = input("You: ").lower()
        battery_level -= 1  # every interaction uses battery

        if "bye" in u or "exit" in u:
            reply = "Bye friend! 😊"
            print(f"Robot: {reply}")
            save_chat_log(u, reply)
            break

        elif "hii" in u or "hello" in u:
            reply = f"Hello {name}! I am {robot}, your AI robot!"
            print(f"Robot: {reply}")
            save_chat_log(u, reply)

        elif "who am i" in u:
            reply = f"You are my {age} years old best friend {name}!"
            print(f"Robot: {reply}")
            save_chat_log(u, reply)

        elif "how are you" in u:
            mood = detect_mood(u)
            if mood == "happy":
                reply = "Nice! Main bhi khush hoon 😄"
            elif mood == "sad":
                reply = "Ohh... Koi baat nahi, sab theek hoga 💖"
            elif mood == "angry":
                reply = "Shant ho ja dost 😅"
            else:
                reply = "Main theek hoon! Aap kaise ho?"
            print(f"Robot: {reply}")
            save_chat_log(u, reply)

        else:
            reply = "Mujhe samajh nahi aaya."
            print(f"Robot: {reply}")
            save_chat_log(u, reply)

        battery_check()

# ---------------------------
#  SENSOR DETECTION MODE
# ---------------------------
def detect_mode():
    global battery_level
    times = int(input("Kitni baar detect karna hai? "))
    for _ in range(times):
        sensor = random.choice(sensor_data)
        action = robot_decision(sensor)
        print(f"[Sensor]: {sensor}  --> [Action]: {action}")
        battery_level -= 2
    battery_check()

# ---------------------------
#  MAIN PROGRAM
# ---------------------------
print(f"\n🤖 I am {robot}, your AI robot!")
battery_check()

while True:
    command = input("\nYou (command): ").lower()
    if "exit" in command:
        print("👋 Goodbye! Shutting down...")
        break
    elif "talk" in command or "chat" in command:
        chat()
    elif "detect" in command:
        detect_mode()
    elif "recharge" in command:
        recharge()
    else:
        print("Robot: Command not recognized. Options: talk/chat, detect, recharge, exit.")
        
