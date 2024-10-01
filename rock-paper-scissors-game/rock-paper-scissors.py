import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.master.geometry("1270x720")
        self.master.configure(bg="#2C3E50")

        self.user_score = 0
        self.computer_score = 0

        # Title Label
        self.title_label = tk.Label(master, text="Rock-Paper-Scissors", font=("Helvetica", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.title_label.pack(pady=10)

        # Instruction Label
        self.instruction_label = tk.Label(master, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.instruction_label.pack(pady=5)

        # Buttons for User Choices
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("Rock"), bg="#27AE60", fg="white")
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("Paper"), bg="#2980B9", fg="white")
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("Scissors"), bg="#E74C3C", fg="white")
        self.scissors_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(master, text="", font=("Helvetica", 14), fg="#ECF0F1", bg="#2C3E50")
        self.result_label.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(master, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.score_label.pack(pady=5)

        # Play Again Button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, bg="#8E44AD", fg="white")
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=f"{self.result_label['text']}\n{result}")
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0 | Computer: 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
