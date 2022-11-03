import random


def welcome():
    print("Welcome to 'Guess the number'!\nPlease,type in your name: ")
    player_name = input()
    wanna_play(player_name)


def wanna_play(player_name):
    print(f"Well, {player_name}, wanna play a little bit? y/n?")
    player_answer = str(input())
    if player_answer == "y":
        game_menu()
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        wanna_play(player_name)


def game_menu():
    print(f"Please choose target difficulty level. Type in:\n"
          f" - 'a' to guess a number between 0 and 10\n"
          f" - 'b' to guess a number between 0 and 100\n"
          f" - 'c' to guess a number between 0 and 1000\n"
          f" - 'e' if you've changed your mind and wanna get out of here")
    player_answer = str(input())
    if player_answer == "a":
        game_a()
    elif player_answer == "b":
        game_b()
    elif player_answer == "c":
        game_c()
    elif player_answer == "e":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        game_menu()


def game_a():
    number_a = random.randint(0, 10)
    digits_taken = 0
    print("I am thinking of a number between 0 and 10. Can you guess?")
    for digits_taken in range(6):
        print("Your guess: ")
        player_guess = int(input())
        if player_guess < number_a:
            print("Your digit is too small.")
        elif player_guess > number_a:
            print("That's too big.")
        elif player_guess == number_a:
            break
    if player_guess == number_a:
        digits_taken = str(digits_taken + 1)
        print(f"Great! You've passed in {digits_taken} guesses.")
        restart()
    elif player_guess != number_a:
        number_a = str(number_a)
        print(f"Alas. The number was: {number_a}")
        restart()


def game_b():
    number_b = random.randint(0, 100)
    digits_taken = 0
    print("I am thinking of a number between 0 and 100. Can you guess?")
    for digits_taken in range(11):
        print("Your guess: ")
        player_guess = int(input())
        if player_guess < number_b:
            print("Your digit is too small.")
        elif player_guess > number_b:
            print("That's too big.")
        elif player_guess == number_b:
            break
    if player_guess == number_b:
        digits_taken = str(digits_taken + 1)
        print(f"Great! You've passed in {digits_taken} guesses.")
        restart()
    elif player_guess != number_b:
        number_a = str(number_b)
        print(f"Alas. The number was: {number_a}")
        restart()


def game_c():
    number_c = random.randint(0, 1000)
    print("I am thinking of a number between 0 and 1000. Can you guess?")
    for digits_taken in range(21):
        print("Your guess: ")
        player_guess = int(input())
        if player_guess < number_c:
            print("Your digit is too small.")
        elif player_guess > number_c:
            print("That's too big.")
        elif player_guess == number_c:
            break
    if player_guess == number_c:
        digits_taken = str(digits_taken + 1)
        print(f"Great! You've passed in {digits_taken} guesses.")
        restart()
    elif player_guess != number_c:
        number_a = str(number_c)
        print(f"Alas. The number was: {number_a}")
        restart()


def restart():
    print("Play again? y/n")
    player_answer = str(input())
    if player_answer == "y":
        game_menu()
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        restart()


if __name__ == '__main__':
    welcome()
