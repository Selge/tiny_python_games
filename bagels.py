import random
import time

from MainMenu import welcome, play_again


def get_secret_num(NUM_DIGITS):
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You got it!"

    clues = []
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


def prompt(NUM_DIGITS):
    print(f"I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.")
    time.sleep(2)
    print("Here are some clues:\n"
          "When I say:      That means:\n"
          " 'Pico'          One digit is correct but in the wrong position.\n"
          " 'Fermi'         One digit is correct and in the right position.\n"
          " 'Bagels'        No digit is correct.\n"
          f"Please, note that each your guess must be a {NUM_DIGITS}-digit number,\n"
          "otherwise the guess will not work out.")


def difficulty():
    NUM_DIGITS = 0
    MAX_GUESS = 0
    iq_levels = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}
    difficulty = 'X'
    while difficulty not in iq_levels.keys():
        print('Enter difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
        match difficulty:
            case 'E':
                NUM_DIGITS = 3
                MAX_GUESS = 10
            case 'M':
                NUM_DIGITS = 4
                MAX_GUESS = 8
            case 'H':
                NUM_DIGITS = 5
                MAX_GUESS = 5

        return NUM_DIGITS, MAX_GUESS


def pico_fermi_bagels():
    NUM_DIGITS, MAX_GUESS = difficulty()
    prompt(NUM_DIGITS)
    while True:
        secret_num = get_secret_num(NUM_DIGITS)
        print(f"I have thought up a number. You have {MAX_GUESS} guesses to get it.")

        guesses_taken = 1
        while guesses_taken <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not is_only_digits(guess):
                print(f"Guess #{guesses_taken}: ")
                guess = input()

            print(get_clues(guess, secret_num))
            guesses_taken += 1

            if guess == secret_num:
                break
            if guesses_taken > MAX_GUESS:
                print(f"You ran out of guesses. The answer was {secret_num}.")

        play_again(pico_fermi_bagels)


if __name__ == '__main__':
    welcome("Welcome to the 'Bagels'!", pico_fermi_bagels)
