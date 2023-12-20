import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice: Rock, Paper, or Scissors\n").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    game_rules = {
        ("Rock", "Scissors"): "You win!",
        ("Paper", "Rock"): "You win!",
        ("Scissors", "Paper"): "You win!",
        ("Scissors", "Rock"): "Computer wins!",
        ("Rock", "Paper"): "Computer wins!",
        ("Paper", "Scissors"): "Computer wins!",
    }

    if user_choice == computer_choice:
        return "It's a tie!"
    else:
        return game_rules.get((user_choice, computer_choice), "Invalid choice!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break
