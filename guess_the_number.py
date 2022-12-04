import random

from MainMenu import welcome, play_again


def guess_the_number():
    print("Please choose target difficulty level. Type in:\n"
          " - 'a' to guess a number between 0 and 10\n"
          " - 'b' to guess a number between 0 and 100\n"
          " - 'c' to guess a number between 0 and 1000\n"
          " - 'e' if you've changed your mind and wanna get out of here")
    player_answer = str(input())
    match player_answer:
        case "a":
            game_a()
        case "b":
            game_b()
        case "c":
            game_c()
        case "e":
            print("Well, see ya later! Bye!")
            exit()
        case _:
            print("Please, use built-in options!")
            guess_the_number()


def game_a():
    number_a = random.randint(0, 10)
    range_guess = range(6)
    print("I am thinking of a number between 0 and 10. Can you guess?")
    guess(number_a, range_guess)


def game_b():
    number_b = random.randint(0, 100)
    range_guess = range(11)
    print("I am thinking of a number between 0 and 100. Can you guess?")
    guess(number_b, range_guess)


def game_c():
    number_c = random.randint(0, 1000)
    range_guess = range(21)
    print("I am thinking of a number between 0 and 1000. Can you guess?")
    guess(number_c, range_guess)


def guess(number, range_guess):
    digits_taken = 0
    for digits_taken in range_guess:
        print("Your guess: ")
        player_guess = int(input())
        if player_guess < number:
            print("Your digit is too small.")
        elif player_guess > number:
            print("That's too big.")
        elif player_guess == number:
            break
    if player_guess == number:
        digits_taken = str(digits_taken + 1)
        print(f"Great! You've passed in {digits_taken} guesses.")
        play_again(guess_the_number)
    elif player_guess != number:
        number_guess = str(number)
        print(f"Alas. The number was: {number_guess}")
        play_again(guess_the_number)


if __name__ == '__main__':
    welcome("Welcome to 'Guess the number'!", guess_the_number)
