# Number Guessing Game (GUI Version)

This is a simple **Number Guessing Game** built using Python's `tkinter` library for the graphical user interface (GUI). The user guesses a number between 1 and 100, and the game provides feedback ("too high", "too low", or "correct"). The user continues guessing until they find the correct number. After each correct guess, the game asks whether they want to play again.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Data Structures Used](#data-structures-used)
4. [Algorithm](#algorithm)
5. [GUI Design](#gui-design)
6. [How to Run the Game](#how-to-run-the-game)
7. [Requirements](#requirements)
8. [Future Improvements](#future-improvements)

---

## Overview

In this game:
- The **computer** selects a random number between 1 and 100.
- The **user** enters guesses through the GUI, and the game provides hints: 
  - "too high" if the guess is higher than the random number.
  - "too low" if the guess is lower than the random number.
  - "correct" when the user guesses the exact number.
- The game keeps track of rounds and the user’s score.
- After each round, the user is prompted to play again or quit.

---

## Features

- **Graphical User Interface (GUI)**: The game is played via buttons and text fields, making it interactive.
- **Hints**: The game provides hints for each guess (too high, too low).
- **Play Again Option**: After each successful guess, the user can choose to continue playing or exit the game.
- **Score and Rounds**: Displays the number of rounds played and the user's score.
- **Input Validation**: Ensures the user enters valid numeric guesses.

---

## Data Structures Used

1. **Integer Variables**:
   - **random_number**: The computer-generated random number (between 1 and 100).
   - **user_score**: Tracks the number of correct guesses.
   - **rounds**: Tracks the number of rounds played.

2. **String Variables**:
   - Feedback messages like "too high", "too low", and "you guessed it right" are handled as string variables to display hints and results.

3. **Functions**:
   - The game logic (random number generation, user input handling, and determining if the guess is correct) is organized into functions.

---

## Algorithm

The game follows this algorithm:

1. **Generate a Random Number**: 
   - The game uses the `random.randint(1, 100)` function to generate a random number at the start of the game.

2. **Get User Input**:
   - The user enters a guess in the text field.
   - The input is validated to ensure it is a valid number.

3. **Comparison**:
   - The program compares the user's guess with the random number:
     - If the guess is **equal** to the random number, the user wins the round.
     - If the guess is **less** than the random number, the program displays "too low".
     - If the guess is **greater** than the random number, the program displays "too high".

4. **Play Again**:
   - Once the user guesses correctly, the game displays a message and asks if the player wants to play another round.
   - If the user chooses "Yes", a new random number is generated, and the game resets.
   - If the user chooses "No", the game ends and displays the final score.

---

## GUI Design

The game is built using `tkinter`, which allows for a simple, interactive interface. Here’s a breakdown of the GUI:

1. **Main Window**:
   - The window is created using `tk.Tk()` and is titled "Number Guessing Game".
   
2. **Input Field** (`Entry` widget):
   - The user enters their guess in this text box.

3. **Buttons**:
   - **Submit Button**: Submits the user's guess.
   - **Yes/No Buttons**: After guessing correctly, these buttons prompt the user to either play again or quit.

4. **Labels**:
   - **Instruction Label**: Instructs the user to enter a number between 1 and 100.
   - **Result Label**: Displays hints like "too high", "too low", or "correct".
   - **Score Label**: Shows the number of rounds played and the user's current score.

---

## How to Run the Game

### 1. Clone the Repository

```bash
git clone <https://github.com/Bakar12/NumberGuessingGamel>
```
###  2. Install Dependencies
Ensure you have Python 3.x installed. The game uses tkinter, which is part of Python’s standard library.

If tkinter is not installed, you can install it using:

bash
Copy code
sudo apt-get install python3-tk
### 3. Run the Game
Run the Python script:

```bash
python NumberGuessingGame.py
```

## Requirements

* Python 3.x: The game is written in Python.
* tkinter: The tkinter library is used to create the GUI, and it is bundled with Python on most systems.
## Future Improvements
Here are some potential improvements that could be added to this game:

1. Adjustable Difficulty: Allow the user to choose different difficulty levels, with varying ranges for the random number.
2. Leaderboard: Keep track of the shortest number of guesses or rounds won.
3. Best of N Rounds: Add an option to play multiple rounds and track the score over a set number of rounds.
4. Timer: Add a timer to see how quickly the user can guess the number.