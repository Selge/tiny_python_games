import random

from MainMenu import welcome, play_again

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You got it!"

    clues = ()
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"

    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    welcome("Welcome to the 'Bagels'!", bagels)
