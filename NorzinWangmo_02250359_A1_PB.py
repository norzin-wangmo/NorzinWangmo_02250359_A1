import random

# 1. Guess Number Game
def guess_number_game():
    #Play a number guessing game between 1 and 100.
    print("\n Welcome to the Guess Number Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1–100): "))
            if guess < 1 or guess > 100:
                print("exit Please enter a number between 1 and 100.")
                continue

            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f" Correct! The number was {number}. You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("! Invalid input. Please enter a valid integer.")


# 2. Rock Paper Scissors Game
def rock_paper_scissors():
    """Play a rock-paper-scissors game against the computer."""
    print("\n Welcome to Rock Paper Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to stop): ").lower().strip()

        if user_choice == 'exit':
            print("\n Final Results:")
            print(f"You won {user_wins} times.")
            print(f"Computer won {computer_wins} times.")
            print(f"Total rounds played: {rounds}\n")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f" Computer chose: {computer_choice}")
        rounds += 1

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print(" You win this round!")
            user_wins += 1
        else:
            print(" Computer wins this round!")
            computer_wins += 1


# Main Menu
def main():
    while True:
        print("\nSelect a game (1–3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit program")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Goodbye! ")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
