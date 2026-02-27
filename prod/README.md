# Prod

A minimal, educational version control system built in Python.

`prod` is a lightweight command-line tool that simulates the core ideas
behind version control systems. It allows you to initialize a
repository, create timestamped commits, and view commit history --- all
using simple filesystem storage and JSON.

This project is designed for learning purposes and does not implement
real file tracking.

------------------------------------------------------------------------

## Features

-   Repository initialization
-   Timestamped commits
-   Commit history logging
-   Hidden metadata directory (`.prod/`)
-   JSON-based persistence
-   No external dependencies (standard library only)

------------------------------------------------------------------------

## Installation

Clone the repository:

    git clone <repo-url>
    cd <repo-folder>

No additional packages are required.

------------------------------------------------------------------------

## Usage

### Initialize a Repository

    python prod.py init

Creates a hidden directory:

    .prod/
        history.json

------------------------------------------------------------------------

### Create a Commit

    python prod.py commit "your commit message"

Each commit stores: - Commit message - ISO-formatted timestamp

------------------------------------------------------------------------

### View Commit History

    python prod.py log

Commits are displayed in reverse chronological order (latest first).

------------------------------------------------------------------------

## Example

    python prod.py init
    python prod.py commit "Initial commit"
    python prod.py commit "Add feature"
    python prod.py log

------------------------------------------------------------------------

## Project Structure

    prod.py
    .prod/
        history.json

------------------------------------------------------------------------

## How It Works

-   `init` creates the `.prod` directory and initializes an empty commit
    history.
-   `commit` appends a message and timestamp to `history.json`.
-   `log` reads and displays stored commits.

All commit data is stored in:

    .prod/history.json

------------------------------------------------------------------------

## Limitations

This is not a full version control system.

It does not: - Track file changes - Store snapshots - Generate commit
hashes - Support branching or merging - Provide diff functionality

It is a conceptual learning tool for understanding: - CLI argument
handling - File I/O - JSON persistence - Repository metadata patterns

------------------------------------------------------------------------

## License

MIT License
