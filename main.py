import random

list_choices = ["paper", "rock", "scissors"]

name = input("Enter your name: ")

print("Hello,", name)

ratings_dict = {}

score = 0

with open('rating.txt', 'r') as ratings:
    for line in ratings:
        ratings_dict[line.split(" ")[0]] = line.split(" ")[1].strip()

# Initializing the Score if the name is in the ratings file:

if name in ratings_dict.keys():

    score = int(ratings_dict[name])

while True:

    computer = random.choice(list_choices)

    user_choice = input("Enter your choice: ")

    if user_choice == "!exit":
        print("Bye!")
        break

    elif user_choice == "!rating":

        print("Your rating: ", score)

    elif computer == user_choice:
        print(f"There is a draw ({computer})")
        score += 50

    elif computer == "rock" and user_choice == "paper":
        print("Well done. The computer chose rock and failed")
        score += 100

    elif computer == "rock" and user_choice == "scissors":
        print("Sorry, but the computer chose rock")

    elif computer == "paper" and user_choice == "scissors":
        print("Well done. The computer chose paper and failed")
        score += 100

    elif computer == "paper" and user_choice == "rock":
        print("Sorry, but the computer chose paper")

    elif computer == "scissors" and user_choice == "rock":
        print("Well done. The computer chose scissors and failed")
        score += 100

    elif computer == "scissors" and user_choice == "paper":
        print("Sorry, but the computer chose scissors")

    else:
        print("Invalid input")
