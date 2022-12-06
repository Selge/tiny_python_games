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


def is_only_digits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


if __name__ == '__main__':
    welcome("Welcome to the 'Bagels'!", bagels)
