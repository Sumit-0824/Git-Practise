import random

# Dictionary with scrambled words and their possible valid words
d = {
    "tca": ["cat", "act"],
    "lpepa": ["apple"],
    "ateb": ["beat", "beta"],
    "rcsa": ["scar", "cars", "arcs"],
    "edr": ["red"],
    "tsae": ["seat", "east"],
    "rcae": ["care", "race"],
    "tloh": ["holt", "loth"],
    "prsae": ["parse", "spare", "spear", "pears"],
    "kool": ["look"],
    "pale": ["leap", "pale", "plea"],
    "arc": ["car", "arc"],
    "plehe": ["help"],
    "tsil": ["list", "slit"],
    "opst": ["post", "spot", "stop", "tops", "pots"],
    "elas": ["sale", "seal"],
    "trit": ["tirt", "trit"],
    "draob": ["board", "broad"],
    "nopia": ["piano"],
    "peehs": ["sheep"],
    "mrea": ["ream", "mare"],
    "enot": ["note", "tone"],
    "dgo": ["dog", "god"],
    "hsif": ["fish"],
    "kciuq": ["quick"]
}


def play_game():
    chances = 10  # Number of chances
    score = 0  # Track the score

    # Start the game loop with 10 chances
    while chances > 0:
        # Choose a random scrambled word from the dictionary
        scrambled_word, valid_words = random.choice(list(d.items()))

        # Show the scrambled word to the player
        print(f"\nScrambled word: {scrambled_word}")

        # Prompt the user to guess a valid word
        guess = input("Guess a valid word: ").lower().strip()

        # Check if the guess is correct
        if guess in valid_words:
            print(f"Correct! {guess} is a valid word.")
            score += 1  # Increment score for a correct guess
        else:
            print(f"Oops! {guess} is not a valid word. The valid words are: {', '.join(valid_words)}")

        chances -= 1  # Reduce a chance after each attempt

        # Provide feedback on the remaining chances
        print(f"Remaining chances: {chances}")

    # Game over
    print("\nGame Over!")
    print(f"Your score: {score} out of 10")


# Run the game
if __name__ == "__main__":
    play_game()
