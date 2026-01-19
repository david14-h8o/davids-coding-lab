import random

def play_game():
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

    for attempt in range(1, 8):
        guess = int(input(f"Attempt {attempt}: "))
        if guess == number:
            print("🎉 You guessed it!")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"😢 Game over. The number was {number}.")

play_game()