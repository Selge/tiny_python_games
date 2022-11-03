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
    print(f"{player_name}, please choose target difficulty level. Type in:"
          f" - 'a' to guess a number between 0 and 10"
          f" - 'b' to guess a number between 0 and 100"
          f" - 'c' to guess a number between 0 and 1000"
          f" - 'e' if you've changed your mind and wanna get out of here")
    player_answer = str(input())
    if player_answer == "a":
        pass
    elif player_answer == "b":
        pass
    elif player_answer == "e":
        print("Well, see ya later! Bye!")
        exit()
    else:
        print("Please, use built-in options!")
        wanna_play(player_name)


print("I am thinking of a number between 0 and 10. Can you guess?")


welcome()
