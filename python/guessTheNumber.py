import random


def guessTheNumber():
    numberToGuess = random.randint(1, 100)
    numberOfTries = 0
    while True:
        userGuess = int(input("Guess a number between 1 and 100: "))
        numberOfTries += 1
        if userGuess < numberToGuess:
            print("Too low!")
        elif userGuess > numberToGuess:
            print("Too high!")
        else:
            print(
                f"Congratulations! You've guessed the number in {numberOfTries} tries."
            )
            break


if __name__ == "__main__":
    guessTheNumber()
