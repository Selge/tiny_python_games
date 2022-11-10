import os


def welcome():
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
            return os.system("coin_flip.py")
        case 'd':
            return os.system("dragon_cave.py")
        case 'g':
            return os.system("guess_the_number.py")
        case 'e':
            exit()
        case 'h':
            os.system("hangman.py")
        case 'r':
            pass
        case 's':
            pass
        case 't':
            pass
        case _:
            print("Please, use built-in options!")


if __name__ == '__main__':
    welcome()
