import os
import json
import sys
from datetime import datetime

def init():

    if os.path.exists(".prod"):
        print("Repository already initialized.")
        return
    
    os.mkdir(".prod")
    
    with open(".prod/history.json", "w") as f:
        json.dump({"commits" : []}, f)

    print("Initialized the repository successfully")

def commit(message):

    if not os.path.exists(".prod"):
        print("Not a prod repository. Run prod init first.")
        return

    try:
        with open(".prod/history.json", "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = {"commits": []}


    commit_data = {
        "message": message,
        "time": datetime.now().isoformat()
    }

    data["commits"].append(commit_data)

    with open(".prod/history.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Committed:", message)

def log():
    if not os.path.exists(".prod"):
        print("Not a prod repository.")
        return

    with open(".prod/history.json", "r") as f:
        data = json.load(f)

    commits = data["commits"]

    if not commits:
        print("No commits yet.")
        return

    for i, commit in enumerate(reversed(commits), 1):
        print(f"commit {i}")
        print(f"Message: {commit['message']}")
        print(f"Time: {commit['time']}")
        print("-" * 30)

if (len(sys.argv) == 2) and (sys.argv[1] == "init"):
    init()

elif (len(sys.argv)== 2) and (sys.argv[1] == "log"):
    log()

elif (len(sys.argv) > 2) and (sys.argv[1] == "commit"):
    commit(sys.argv[2])