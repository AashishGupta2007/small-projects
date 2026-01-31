import json
import os
import sys
import datetime

data_file = "data.json" #connection with the database : json file

def load_data():  #for accesssing the database
    if not os.path.exists(data_file):
        return {}

    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    
def save_data(data):  #for saving everything after changes in database
    with open(data_file, "w",) as f:
        json.dump(data, f, indent = 4)

def normalize(habit_name):  #avoid repeating data
    return habit_name.lower().replace(" ", "_")

def add_habit(habit_name):  #adding habits

    data = load_data()
    key = normalize(habit_name)

    if key in data:
        print("Habit already exists")
        return
    
    today = datetime.date.today().isoformat()

    data[key] = {
        "last done" : today,
        "longest streak" : 0
    }

    save_data(data)
    print(f"Added Habit : {habit_name}")


def reset_habit(habit_name):
    data = load_data()
    key = normalize(habit_name)

    if key not in data:
        add_habit(habit_name)
        print("Habit did not exist. Added now.")
        return
    
    today = datetime.date.today().isoformat()
    data[key]["last done"] = today

    save_data(data)
    print("Habit has been reset to today")

    
def show_status():  #for viewing 
    data = load_data()
    today = datetime.date.today()

    if not data:
        print("No habits stored yet.")
        return
    for habit, info in data.items():
        last_done = datetime.date.fromisoformat(info["last done"])
        current_streak = (today - last_done).days
        longest_streak = info["longest streak"]

        # Update longest streak if current is bigger
        if current_streak > longest_streak:
            data[habit]["longest streak"] = current_streak
            save_data(data)
            longest_streak = current_streak

        habit_name = habit.replace("_", " ").title()
        print(f"{habit_name}: {current_streak} days clean (best: {longest_streak})")

import json
import os
import sys
import datetime

data_file = "data.json"

def load_data():
    if not os.path.exists(data_file):
        return {}
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

def normalize(habit_name):
    return habit_name.lower().replace(" ", "_")

def add_habit(habit_name):
    data = load_data()
    key = normalize(habit_name)
    if key in data:
        print("Habit already exists")
        return
    today = datetime.date.today().isoformat()
    data[key] = {"last done": today, "longest streak": 0}
    save_data(data)
    print(f"Added Habit: {habit_name}")

def reset_habit(habit_name):
    data = load_data()
    key = normalize(habit_name)
    if key not in data:
        add_habit(habit_name)
        print("Habit did not exist. Added now.")
        return
    today = datetime.date.today().isoformat()
    data[key]["last done"] = today
    save_data(data)
    print(f"Habit '{habit_name}' has been reset to today")

def show_status():
    data = load_data()
    today = datetime.date.today()
    if not data:
        print("No habits stored yet.")
        return
    for habit, info in data.items():
        last_done = datetime.date.fromisoformat(info["last done"])
        current_streak = (today - last_done).days
        longest_streak = info["longest streak"]
        if current_streak > longest_streak:
            data[habit]["longest streak"] = current_streak
            save_data(data)
            longest_streak = current_streak
        habit_name = habit.replace("_", " ").title()
        print(f"{habit_name}: {current_streak} days clean (best: {longest_streak})")

# ------------------ COMMAND HANDLER ------------------
if len(sys.argv) >= 2:
    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        habit = " ".join(sys.argv[2:])
        add_habit(habit)

    elif command == "reset" and len(sys.argv) >= 3:
        habit = " ".join(sys.argv[2:])
        reset_habit(habit)

    elif command == "status":
        show_status()

    else:
        print("Invalid command. Use: add <habit>, reset <habit>, or status.")

else:
    print("Please enter a command: add <habit>, reset <habit>, or status.")



