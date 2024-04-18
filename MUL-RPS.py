import random

def select_game_mode():
    while True:
        mode = input("Select game mode (1 player or 2 player): ").lower()
        if mode == '1 player' or mode == '2 player':
            return mode
        else:
            print("Invalid choice. Please enter '1 player' or '2 player'.")

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    mode = select_game_mode()
    while True:
        if mode == '1 player':
            player1_choice = get_player_choice()
            computer_choice = get_computer_choice()
            print(f"You chose {player1_choice}, and the computer chose {computer_choice}.")
            print(determine_winner(player1_choice, computer_choice))
        else:
            player1_choice = get_player_choice()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            player2_choice = get_player_choice()
            print(f"Player 1 chose {player1_choice}, and Player 2 chose {player2_choice}.")
            print(determine_winner(player1_choice, player2_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()
