# Number Guessing Game
import random
import tkinter as tk
from tkinter import messagebox


# Function to get the random number
def get_random_number():
    return random.randint(1, 100)


# Function to determine if the user's guess is correct
def determine_guess(user_guess, random_num):
    if user_guess == random_num:
        return "You guessed it right!"
    elif user_guess < random_num:
        return "Your guess is too low!"
    else:
        return "Your guess is too high!"


# Function to handle user guess and update results
def handle_guess():
    global random_number, rounds, user_score

    try:
        # Get the user's guess and convert it to an integer
        user_guess = int(user_guess_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return

    rounds += 1
    result = determine_guess(user_guess, random_number)

    if result == "You guessed it right!":
        user_score += 1
        result_label.config(text=f"{result} The correct number was {random_number}!")
        play_again_frame.pack(pady=20)
    else:
        result_label.config(text=result)

    # Update score and rounds
    score_label.config(text=f"Rounds Played: {rounds}\nYour Score: {user_score}")
    user_guess_entry.delete(0, tk.END)


# Function to handle play again decision
def play_again_decision(decision):
    global random_number

    if decision == "yes":
        random_number = get_random_number()
        result_label.config(text="Make your guess!")
        play_again_frame.pack_forget()
    else:
        messagebox.showinfo("Game Over",
                            f"Final Score:\nRounds Played: {rounds}\nYour Score: {user_score}")
        root.quit()


# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Initialize variables for scores and rounds
user_score = 0
rounds = 0

# Generate the first random number
random_number = get_random_number()

# Create and place GUI components

# Title Label
title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 24))
title_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="Enter a number between 1 and 100:", font=("Arial", 16))
instruction_label.pack(pady=10)

# Input Field for user guess
user_guess_entry = tk.Entry(root, font=("Arial", 16))
user_guess_entry.pack(pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 16), command=handle_guess)
submit_button.pack(pady=10)

# Result Label to show the round result
result_label = tk.Label(root, text="Make your guess!", font=("Arial", 16))
result_label.pack(pady=20)

# Score Label to display the current scores and rounds played
score_label = tk.Label(root, text=f"Rounds Played: {rounds}\nYour Score: {user_score}", font=("Arial", 14))
score_label.pack(pady=20)

# Frame for Play Again buttons (Yes/No)
play_again_frame = tk.Frame(root)

# Yes Button
yes_button = tk.Button(play_again_frame, text="Yes", font=("Arial", 14), width=10,
                       command=lambda: play_again_decision("yes"))
yes_button.grid(row=0, column=0, padx=10)

# No Button
no_button = tk.Button(play_again_frame, text="No", font=("Arial", 14), width=10,
                      command=lambda: play_again_decision("no"))
no_button.grid(row=0, column=1, padx=10)

# Run the main event loop
root.mainloop()
