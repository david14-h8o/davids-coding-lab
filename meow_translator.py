import random

# Dictionary of cat sounds and their meanings
MEOW_DICTIONARY = {
    "meow": [
        "Feed me, human.",
        "I demand attention.",
        "Open the door. Now."
    ],
    "mrrp": [
        "Hello there!",
        "I’m feeling playful.",
        "Pet me, but only three times."
    ],
    "purr": [
        "Life is good.",
        "I trust you.",
        "Keep doing what you’re doing."
    ],
    "hiss": [
        "Back off!",
        "I don’t like this.",
        "You shall not pass."
    ],
    "chirp": [
        "Look at that bird!",
        "Hunter mode activated.",
        "I’m excited!"
    ],
    "yowl": [
        "Where are you?",
        "I’m lonely.",
        "This is unacceptable."
    ]
}

def translate_cat_sound(sound: str) -> str:
    """Translate a cat sound into human language."""
    sound = sound.lower().strip()
    if sound in MEOW_DICTIONARY:
        return random.choice(MEOW_DICTIONARY[sound])
    else:
        return "Unknown feline sound. Try again."

def interactive_translator():
    print("🐱 Welcome to the Meow Translator!")
    print("Type a cat sound (meow, mrrp, purr, hiss, chirp, yowl). Type 'quit' to exit.\n")
    
    while True:
        user_input = input("Cat says: ")
        if user_input.lower() == "quit":
            print("Goodbye, human. 🐾")
            break
        translation = translate_cat_sound(user_input)
        print(f"Translation: {translation}\n")

if __name__ == "__main__":
    interactive_translator()