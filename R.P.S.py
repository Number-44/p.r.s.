import random
import tkinter as tk
from tkinter import messagebox

def play(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You won!"
    else:
        result = "You lost!"
    
    # Show the result
    messagebox.showinfo("Result", f"Computer chose {computer_choice}.\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Add buttons for user choices
choices = ['Rock', 'Paper', 'Scissors']
for choice in choices:
    button = tk.Button(window, text=choice, command=lambda c=choice: play(c), width=20)
    button.pack(pady=10)

# Run the GUI
window.mainloop()
