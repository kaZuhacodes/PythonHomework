import random

choices = ['rock', 'paper', 'scissors']
winning_conditions = {
    "rock": "scissors", 
    "paper": "rock",    
    "scissors": "paper" 
}

player = 0
computer = 0
while player < 5 and computer < 5:
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice: ")

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Tie!")
    elif winning_conditions[player_choice] == computer_choice:
        print("You won!")
        player += 1
    else: 
        print("You lost!")
        computer += 1
    
    print(f"Score: You {player} - {computer} Computer\n")

if player == 5:
    print("Congratulations! You won the game!")
else:
    print("Game over! The computer wins!")