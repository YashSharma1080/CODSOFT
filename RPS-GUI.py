import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to handle the game logic
def play_game(player_choice):
    computer_choice = get_computer_choice()
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

# Creating the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Creating buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

# Running the application
root.mainloop()
