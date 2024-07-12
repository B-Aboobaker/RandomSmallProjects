import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    print("--------Welcome to Rock, Paper, Scissors. Let the game begin--------")

    while player not in choices:
        player = input("You choose Rock, Paper or Scissors? ").lower()

    if player == computer:
        print("Computer chose:", computer)
        print("Player chose:", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You lose! Paper covers Rock")
        if computer == "scissors":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You win! Rock smashes Scissors")

    elif player == "scissors":
        if computer == "rock":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You lose! Rock Smashes Scissors")
        if computer == "paper":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You win! Scissors cut Paper")

    elif player == "paper":
        if computer == "scissors":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You lose! Scissors cut Paper")
        if computer == "rock":
                print("Computer chose:", computer)
                print("Player chose:", player)
                print("You win! Paper covers Rock")

    play_again = input("Would you like to play again? (Y for yes or N for No): ").lower()

    if play_again != "y":
        break
print("Bye, see you next time.")
