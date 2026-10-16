"""
Day 4 Project: Rock, Paper, Scissors

Background:
    Play the classic hand game against the computer. You pick 0 (Rock),
    1 (Scissors) or 2 (Paper); the computer picks randomly. The rules:
        Rock beats Scissors
        Scissors beats Paper
        Paper beats Rock
    The program validates your input, shows both choices and announces the
    result: win, lose or draw.

Concepts practised:
    The random module, functions, input validation, comparison and logical
    operators.
"""

import random

computer_choice = random.randint(0, 2)
print("Rule of the Game:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
human_choice = input("What do you choose? 0 for Rock, 1 for Scissors, 2 for Paper?\n")


def choice(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Scissors"
    elif number == 2:
        return "Paper"
    else:
        return "Wrong Choice"


if human_choice != "0" and human_choice != "1" and human_choice != "2":
    print("\nWarning: Provide one number (0 or 1 or 2)")
else:
    human_choice = int(human_choice)

    print(f"\nYou chose: {choice(human_choice)}\nComputer chose: {choice(computer_choice)}\n")

    if (human_choice == 0 and computer_choice == 1) \
            or (human_choice == 1 and computer_choice == 2) \
            or (human_choice == 2 and computer_choice == 0):
        print("Result: Yayyy! You Win!")
    elif human_choice == computer_choice:
        print("Result: It's a Draw. Try again!")
    else:
        print("Result: You Lose! Try again!")
