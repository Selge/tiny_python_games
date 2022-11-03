import random


digits_written = 0


def welcome():
    print("Welcome to 'Guess the number'!\nPlease,type in your name: ")
    player_name = input()
    print(f"Well, {player_name}, wanna play a little bit? y/n?")
    player_answer = str(input())
    if player_answer == "y":
        game_menu()
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()


def game_menu():

    print("I am thinking of a number between 0 and 10. Can you guess?")


welcome()
