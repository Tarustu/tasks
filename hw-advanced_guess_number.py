# -----------------------------
# Advanced Number Guessing Game
# -----------------------------

import random

# -----------------------------
# Game Setup
# -----------------------------

# TODO 1: Ask the player for the minimum and maximum values for the range.
min_value = int(input("min value?"))
max_value = int(input("max value"))

# TODO 2: Generate a random number within the custom range.
# Hint: use the random.randint() function
random_number = random.randint(min_value,max_value)

difficulty=input("choose a difficulty level (easy, medium, hard).")# TODO 3: Ask the player to choose a difficulty level (easy, medium, hard).
if difficulty=="easy":# Based on their choice, set the number of attempts allowed.
    attempts = 10
    print("you have 10 attempts") # Replace None with logic to set attempts based on difficulty
elif difficulty=="medium":
     attempts = 7
     print("you have 7 attempts")
elif difficulty ("hard"):
     attempts = 5
     print("you have 5 attempts")
else:
    print("please choose a difficulty")

# Inform the player about the game
print(
    f"Guess the number (between {min_value} and {max_value}). You have {attempts} attempts."
)

# -----------------------------
# Main Game Logic
# -----------------------------

# Keep track of the player's guesses
guesses = []  # TODO 4: Use this list to store each guess made by the player

while attempts > 0:
    try:
        # TODO 5: Ask the player to enter their guess and convert it to an integer.
        guess = int(input("Guess a number"))  # Replace None with input logic

        guesses.append(guess)# TODO 6: Add the guess to the guesses list
        # Use the append() method to add the guess to the list.

        # Check if the guess is correct
        if guess==random_number:  # Replace False with the condition to check if guess == random_number
            print("You guessed it! Well done.")
            break
        elif (guess<random_number):  # Replace False with the condition to check if guess < random_number
            print("Too low.")
        else:
            print("Too high.")

        difference = abs(guess - random_number)
        if difference<=3:
            print("Hot!")
                # TODO 7: Add proximity hints (optional)
        else:
            print("Cold!")        # Example: Print "Hot!" if the guess is within 3, "Cold" if it's more than 10 away.

        # Decrement attempts
        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    except ValueError:
        # Handle invalid input
        print("Please enter a valid number.")

# -----------------------------
# End of Game
# -----------------------------

if attempts==0:
    print(f"You've ran out of attempts, Better luck next time, The correct number is:{random_number}")# TODO 8: If the player runs out of attempts, display the correct number.
# Hint: Use an if condition to check if attempts == 0

print(f"Your guesses: {guesses}")
# TODO 9: At the end of the game, display the list of guesses made by the player.
# Example: print(f"Your guesses: {guesses}")
