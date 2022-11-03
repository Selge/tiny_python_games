import random


digits_written = 0


def welcome():
    print("Welcome to 'Guess the number'!\nPlease,type in your name: ")
    player_name = input()
    wanna_play(player_name)


def wanna_play(player_name):
    print(f"Well, {player_name}, wanna play a little bit? y/n?")
    player_answer = str(input())
    if player_answer == "y":
        game_menu(player_name)
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        wanna_play(player_name)


def game_menu(player_name):
    print(f"{player_name}, please choose target difficulty level. Type in:\n"
          f" - 'a' to guess a number between 0 and 10\n"
          f" - 'b' to guess a number between 0 and 100\n"
          f" - 'c' to guess a number between 0 and 1000\n"
          f" - 'e' if you've changed your mind and wanna get out of here")
    player_answer = str(input())
    if player_answer == "a":
        pass
    elif player_answer == "b":
        pass
    elif player_answer == "c":
        pass
    elif player_answer == "e":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        game_menu(player_name)


def game_a(player_guess):
    number_a = random.randint(0, 10)
    print("I am thinking of a number between 0 and 10. Can you guess?")
    guess()
    if player_guess < number_a:
        print("Your digit is too small.")
        print("Try again? y/n")
        player_answer = str(input())
        if player_answer == "y":
            guess()
    elif player_guess > number_a:
        print("That's too big.")


def game_b(player_guess):
    number_b = random.randint(0, 100)
    print("I am thinking of a number between 0 and 100. Can you guess?")
    guess()
    if player_guess < number_b:
        print("Your digit is too small.")
        guess()
    elif player_guess > number_b:
        print("That's too big.")


def game_c(player_guess):
    number_c = random.randint(0, 1000)
    print("I am thinking of a number between 0 and 1000. Can you guess?")
    guess()
    if player_guess < number_c:
        print("Your digit is too small.")
        guess()
    elif player_guess > number_c:
        print("That's too big.")


def guess():
    print("Your guess: ")
    player_guess = int(input())


def restart(player_name):
    print("Play again? y/n")
    player_answer = str(input())
    if player_answer == "y":
        game_menu(player_name)
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        restart(player_name)


if __name__ == '__main__':
    welcome()
