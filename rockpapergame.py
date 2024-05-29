print("~ROCK PAPER SCISSOR GAME~")


import random

options=("rock","paper","scissors")
running=True

while running:
    user=None
    computer=random.choice(options)

    while user not in options:
        user=input("enter your choice(rock,paper,scissors):")
    print(f"user: {user}")
    print(f"computer: {computer}")

    if(user == computer):
            print("it's a tie")
    elif(user == "rock" and computer == "scissors"):
            print("you win")
    elif(user == "paper" and computer == "rock"):
            print("you win")
    elif(user == "scissors" and computer == "paper"):
            print("you win")
    else:
            print("you lose")

    play_again=input("play again?(y/n):").lower()
    if not play_again == "y":
            running=False
            print("Thanks for playing!!")