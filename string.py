import random
cpu_score=0
user_score=0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        cpu_score=cpu_score
        user_score=user_score
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            cpu_score=cpu_score
            user_score=user_score+1
        else:
            print("Paper covers rock! You lose.")
            cpu_score=cpu_score+1
            user_score=user_score
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            cpu_score=cpu_score
            user_score=user_score+1
        else:
            print("Scissors cuts paper! You lose.")
            cpu_score=cpu_score+1
            user_score=user_score
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            cpu_score=cpu_score
            user_score=user_score+1
        else:
            print("Rock smashes scissors! You lose.")
            cpu_score=cpu_score+1
            user_score=user_score

    play_again = input("Play again? (y/n): ")
    if play_again == "n":
     break
print("CPU",cpu_score)
print("User",user_score)