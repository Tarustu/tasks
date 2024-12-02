# ---------------------------------------------------
# Advanced Hangman with ASCII Art - Exercise Template
# ---------------------------------------------------

import random

# -----------------------------
# Game Setup
# -----------------------------

# TODO 1: Create a list of words for the game.
word_list = [ "apple", "banana", "cherry", "dragon", "eclipse", "forest", "galaxy", "harmony",
    "illusion", "jungle", "kaleidoscope", "labyrinth", "mountain", "nebula", "ocean",
    "paradise", "quasar", "rainbow", "symphony", "treasure", "umbrella", "voyage",
    "whisper", "xenon", "yonder", "zephyr"]  # Add some words

# TODO 2: Randomly select a word from the list.
chosen_word = random.choice(word_list)

# Initialize game variables
# TODO 3: Create a `guessed_word` list with "_" for each letter in the chosen word.
guessed_word = ["_"]*len(chosen_word)

# TODO 4: Set the number of attempts to 6.
attempts = 6

# TODO 5: Create an empty list to keep track of guessed letters.
guessed_letters = []



# TODO 6: Review the ASCII art below, what type of the structure is this?
hangman_stages = [
    """
      _______
      |      
      |      
             
             
             
    """,
    """
      _______
      |     | 
      |      
      O      
             
             
    """,
    """
      _______
      |     | 
      |      
      O      
      |      
             
    """,
    """
      _______
      |     | 
      |      
      O      
     /|      
             
    """,
    """
      _______
      |     | 
      |      
      O      
     /|\     
             
    """,
    """
      _______
      |     | 
      |      
      O      
     /|\     
     /       
    """,
    """
      _______
      |     | 
      |      
      O      
     /|\     
     / \     
    """
]

print("Welcome to Advanced Hangman!")
# TODO 7: Print the word length and the number of attempts.
print(f"The word has {len(chosen_word)} letters. You have {attempts} attempts.\n")

# -----------------------------
# Main Game Logic
# -----------------------------

while attempts > 0:
    # TODO 8: Display the current state of the guessed word and the hangman stage.
    print(" ".join(guessed_word))
    print(hangman_stages[6-attempts])

    # TODO 9: Ask the player to guess a letter and validate the input.
    guess=input("Enter your first letter").lower()

    # TODO 10: Check if the guessed letter has already been guessed.
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # TODO 11: If the guess is correct, update the guessed_word list.
    if guess in chosen_word:
        print(f"Great job! the letter {guess} is in the word ")
        for index, letter in enumerate(chosen_word):
            if letter==guess:
                guessed_word[index]=guess

    # TODO 12: If the guess is incorrect, reduce the number of attempts and notify the player.
    else:
        print(f"Wrong guess! The letter {guess} is not in the word.")
        attempts -= 1

    # TODO 13: Check if the word has been fully guessed.
    if "_" not in guessed_word:
        print(f"Congratulations! You've guessed the word: {chosen_word}")
        break

    print(f"Attempts remaining: {attempts}\n")

   

# -----------------------------
# End of Game
# -----------------------------

# TODO 14: If the player runs out of attempts, show the final hangman stage and the correct word.

if attempts == 0:
    print(f"Game over. The word was: {chosen_word}")