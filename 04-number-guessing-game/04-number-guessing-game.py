"""
Day 04: Number Guessing Game
Generates a random number between 1 and 100 and prompts the user to guess it.
"""

import random


def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=" * 45)
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
    print("=" * 45)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    while True:
        try:
            guess = int(input("Enter your guess -> "))
            attempts += 1

            # 1. Out of Bounds Check
            if guess < 1 or guess > 100:
                print("⚠️  OUT OF BOUNDS! Please enter a number between 1 and 100.\n")
                continue

            # 2. Correct Guess
            if guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! You guessed it right in {attempts} attempt(s)!")
                break
            # 3. Too Low
            elif guess < secret_number:
                print("📉 Too low! Try guessing a higher number.\n")
            # 4. Too High
            else:
                print("📈 Too high! Try guessing a lower number.\n")

        except ValueError:
            print("❌ Invalid input! Please enter a whole number.\n")


if __name__ == "__main__":
    number_guessing_game()