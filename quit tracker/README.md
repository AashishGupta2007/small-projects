# Habit Tracker

A simple command-line habit tracking tool built in Python.

This project allows you to track negative habits (e.g., junk food,
skipped workouts) and maintain streak information using a JSON file for
persistence.

------------------------------------------------------------------------

## Features

-   Track habits with last occurrence date
-   Maintain longest streak data
-   JSON-based storage (`data.json`)
-   Lightweight and minimal
-   No external dependencies (standard library only)

------------------------------------------------------------------------

## Project Structure

    tracker.py
    data.json
    README.md

------------------------------------------------------------------------

## How It Works

The application stores habit data inside:

    data.json

Example structure:

{ "junk_food": { "last done": "2026-01-31", "longest streak": 0 },
"skipped_workout": { "last done": "2026-01-31", "longest streak": 0 } }

Each habit tracks:

-   `last done` → the last date the habit occurred
-   `longest streak` → longest streak achieved

The script reads from and writes to this file to update progress.

------------------------------------------------------------------------

## Usage

Run:

    python tracker.py

Follow the CLI prompts to log habits or check streaks.

------------------------------------------------------------------------

## Purpose

This project demonstrates:

-   File I/O operations
-   JSON data persistence
-   Date handling in Python
-   Simple CLI-based application design

------------------------------------------------------------------------

## Limitations

-   No GUI
-   No database backend
-   No advanced analytics
-   No authentication or multi-user support

This is a minimal learning project focused on core logic and data
handling.

------------------------------------------------------------------------

## License

MIT License
