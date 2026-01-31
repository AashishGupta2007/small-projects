````markdown
# Quit Tracker 🛑

**A simple command-line habit tracker to help you quit bad habits and track your streaks.**  

Keep track of your daily habits, monitor streaks, and stay motivated by seeing your progress over time. All data is stored locally in a JSON file, so it’s lightweight and easy to use.

---

## Features ✅

- **Add habits** you want to quit or monitor.
- **Reset habits** to mark the current day as the last time you did it.
- **Track streaks** and longest streaks automatically.
- **Persistent storage** using a local JSON file (`data.json`).
- Works entirely in the **terminal / command-line** — no GUI required.  

---

## Installation 💻

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
````

2. Navigate to the project folder:

```bash
cd <your-repo>
```

3. Make sure you have **Python 3** installed:

```bash
python3 --version
```

---

## Usage 📝

Run the tracker using Python 3 and the following commands:

### 1. Add a new habit

```bash
python3 tracker.py add "habit name"
```

Example:

```bash
python3 tracker.py add "junk food"
```

Output:

```
Added Habit: junk food
```

---

### 2. Reset a habit

```bash
python3 tracker.py reset "habit name"
```

Example:

```bash
python3 tracker.py reset "junk food"
```

Output:

```
Habit 'junk food' has been reset to today
```

---

### 3. Check your habits status

```bash
python3 tracker.py status
```

Example output:

```
Junk Food: 0 days clean (best: 0)
Doom Scrolling: 3 days clean (best: 5)
```

* **Current streak** = days since the last occurrence
* **Best streak** = longest streak so far

---

## Data Storage 📂

* All habit data is stored in a file called `data.json` in the same folder.
* Example content:

```json
{
    "junk food": {
        "last done": "2026-01-31",
        "longest streak": 0
    },
    "doom scrolling": {
        "last done": "2026-01-29",
        "longest streak": 5
    }
}
```

* `last done` = the last date you performed/reset the habit
* `longest streak` = your personal best streak

---

## How it works ⚙️

1. **Add a habit** → initializes with today’s date and 0 streak.
2. **Reset a habit** → updates the last done date to today.
3. **Show status** → calculates current streaks and updates longest streak if necessary.
4. **Data is persistent** → all changes are saved immediately to `data.json`.

---

## Future Improvements 🌟

* Menu-based CLI for easier use
* Visual streaks with emojis 🔥💪
* Weekly/monthly habit reports
* Support for good habits (positive tracking)

---

## License 📄

This project is **open source**. Feel free to use, modify, and share!

```

---
