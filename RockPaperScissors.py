import random

while True:
    #get user choice
    user_action = input("Enter your choice (Rock, Paper or Scissors): ")

    #create array of possible choices
    possible_actions = ["rock", "paper", "scissors"]

    #make computer pick random choice
    computer_actions = random.choice(possible_actions)

    print(f"\nyou chose {user_action}, Computer chose {computer_actions}.\n")

    #Determine the winner
    if user_action == computer_actions:
        print("both players chose" + {user_action}+ ". Its a tie")
    elif user_action == "rock":
        if computer_actions == "scissors":
            print("Rock smashes scissors. You win!!")
        else:
            print("Paper covers rock. You Lose!!!")   
    elif user_action == "paper":
        if computer_actions == "rock":
            print("paper covers rock. You Win!!!")
        else:
            print("Scissors cuts paper. You Lose!!!")
    elif user_action == "scissors":
        if computer_actions == "paper":
            print ("Scissors cuts paper. You Win!!!")
        else:
            print("Rock smashes scissors. You lose!!!")
    
    Play_again = input("Play Again (y/n): ")
    if Play_again.lower() != "y":
        break