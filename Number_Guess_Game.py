import random
def get_attempts(difficulty):
    """Return number of attempts based on difficulty level."""

    if difficulty == "easy":
        return 10
    elif difficulty == "Medium":
        return 8
    elif difficulty == "Hard":
        return 5
    else:
        return 7

print("Welcome to the Number Guessing Game!")
print("Choose a difficulty: Easy,Medium or Hard")

difficulty = input("Enter a difficulty level: ").lower()

number_to_guess = random.randint(1,100)
attempts = get_attempts(difficulty)

print(f"\nI have chosen a number between 1 and 100. You have {attempts} attempts to guess it!")

while attempts > 0:
    try:
        guess = int(input("\nEnter your guess:"))
    except ValueError:
        print("Invalid input! Please enter a number. ")
        continue

    if guess == number_to_guess:
        print(f" Congrats! You guessed the number {number_to_guess}")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    
    else:
        print("Too high! Try again")

    attempts -= 1

    if attempts > 0:
        print(f"Attempts left: {attempts}")

    else:
        print(f"\n Out of attempts! The correct number was {number_to_guess}")





