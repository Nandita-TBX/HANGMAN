# HANGMAN

### A Command-Line Word Guessing Game in Python

A simple command-line Hangman game written in Python. A random word is selected from a predefined list, and the player must guess it one letter at a time before running out of lives. The player starts with 10 lives and loses one for every incorrect guess.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How to Play](#how-to-play)
- [How It Works](#how-it-works)
- [Customizing the Word List](#customizing-the-word-list)
- [Learning Outcomes](#learning-outcomes)

---

## Features

- Random word selection from a predefined word list
- 10 chances to guess the correct word
- Displays the current progress of the word after every guess
- Tracks previously guessed letters
- Prevents repeated guesses so they never cost a life
- Validates user input (single alphabetic characters only)
- Reveals the correct word if the player loses

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 |
| Word selection | `random` module |
| Input handling | `string` module |
| Interface | Command line |

## Getting Started

### Prerequisites

- Python 3 installed on your machine

### Installation

Clone or download this repository:

```bash
git clone https://github.com/<your-username>/Hangman.git
cd Hangman
```

Make sure `Words.py` is in the same directory as `hangman.py`.

### Run

```bash
python hangman.py
```

On some systems you may need to use `python3 hangman.py` instead.

## Project Structure

```
Hangman/
├── hangman.py    # Main game logic
├── Words.py      # List of words used by the game
└── README.md     # Project documentation
```

## How to Play

1. Run the program. A random word is selected and shown as blanks.
2. Enter one letter at a time to guess the word.
3. Correct guesses reveal the letter in its position(s) within the word.
4. Incorrect guesses reduce your remaining lives.
5. Guess the complete word before your lives reach zero to win.

Example session (illustrative output):

```
Lives: 10
Word: _ _ _ _ _ _

Guess a letter: a
Word: _ _ _ _ a _

Guess a letter: z
Wrong guess. Lives left: 9
Guessed letters: a, z
```

## How It Works

1. A word is chosen at random from the list in `Words.py`.
2. The game loops, prompting for a single letter each turn.
3. Input is validated: anything that is not a single letter is rejected.
4. Letters already guessed are rejected without costing a life.
5. A correct guess updates the displayed word; an incorrect guess removes one life.
6. The game ends when the word is fully revealed (win) or lives reach zero (loss, and the word is shown).

## Customizing the Word List

Open `Words.py` and add or remove entries from the word list. The game picks from whatever is in the file, so you can create themed rounds such as animals, countries, or programming terms.

## Learning Outcomes

Through this project, I practised:

- Python functions and loops
- Conditional statements
- Lists and sets
- Random word selection
- String manipulation
- User input validation
