import random

user_won = 0
computer_won = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Exit to stop: ").lower()
    if user_input == "exit":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice= options[random_number]
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_won += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_won += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_won += 1

    else:
        print("You lost!")
        computer_won += 1

print("You won","times.",user_won)
print("The computer won","times.",computer_won)
print("Thanks for playing!")
