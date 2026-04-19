print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")
print("Options are: Rock, Paper, Scissors, or Quit to exit.")

import random

choices = ["rock", "paper", "scissors"]

user_wins = 0
ties = 0
computer_wins = 0

while True:
    user_choice = input("Enter your choice (First letter or whole word): ").lower()
    if user_choice in ["rock", "r"]:
        user_choice = "rock"
    elif user_choice in ["paper", "p"]:
        user_choice = "paper"
    elif user_choice in ["scissors", "s"]:
        user_choice = "scissors"
    elif user_choice in ["quit", "q"]:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose {user_choice}, the computer chose {computer_choice}.")

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    elif user_choice == computer_choice:
        print("Tie")
        ties += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win")
        user_wins += 1
    else:
        print("Computer wins")
        computer_wins += 1

print(f"Your wins: {user_wins}")
print(f"Ties: {ties}")
print(f"Computer wins: {computer_wins}")