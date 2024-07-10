import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    choices_list = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while player_choice not in choices_list:
        player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return player_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player"
    else:
        return "Computer"

def display_scores(player_score, computer_score):
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

def rock_paper_scissors_game():
    print("Welcome to Rock, Paper, Scissors Game!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")

        display_scores(player_score, computer_score)

        play_again = input("Do you want to play another round? (yes or no): ").lower()
        if play_again != "yes":
            break

    print("Final Scores:")
    display_scores(player_score, computer_score)
    print("Thank you for playing!")

rock_paper_scissors_game()
