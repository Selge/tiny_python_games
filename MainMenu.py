import os
import time

def menu():
    print("Welcome to the 'Tiny Python games'!\nPlease,type in your name: ")
    player_name = input()
    wanna_play(player_name)


def wanna_play(player_name):
    print(f"Well, {player_name}, wanna play a little bit? y/n?")
    player_answer = str(input())
    match player_answer:
        case "y":
            game_menu()
        case "n":
            print("Well, see ya later! Bye!")
            exit()
        case _:
            print("Please, use built-in options!")
            wanna_play(player_name)


def game_menu():
    print("Welcome to the 'Tiny Python games shell'!\n"
          "Please, select a game from the list below:\n"
          " - a 'Dodger' \n"
          " - b 'Bagels' \n"
          " - c 'Coin flip' \n"
          " - d 'Dragon cave' \n"
          " - g 'Guess the number' \n"        
          " - h 'Hangman' \n"
          " - r 'Reversi' \n"
          " - s 'Sonar Treasure Hunt' \n"
          " - t 'Tic Tac Toe' \n"
          " - e to exit the program")

    choice = str(input())

    match choice:
        case 'a':
            pass
        case 'b':
            pass
        case 'c':
            os.system("coin_flip.py")
        case 'd':
            os.system("dragon_cave.py")
        case 'g':
            os.system("guess_the_number.py")
        case 'e':
            exit()
        case 'h':
            os.system("hangman.py")
        case 'r':
            pass
        case 's':
            pass
        case 't':
            os.system("tictactoe.py")
        case _:
            print("Please, use built-in options!")


def welcome(game_name: str, file_game):
    print(game_name)
    time.sleep(3)
    file_game()


def play_again(game):
    print("Wanna play again? (y/n)\n"
          "Or type in 'm' to get back to the main menu")
    player_answer = input().lower()
    match player_answer:
        case 'y':
            game()
        case 'n':
            print("Well, good luck next time!")
            exit()
        case "m":
            os.system("MainMenu.py")
        case _:
            exit()


if __name__ == '__main__':
    menu()
