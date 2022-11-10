import os


def welcome():
    print("Welcome to the 'Tiny Python games shell'!\n"
          "Please, select a game from the list below:\n"
          " - g 'Guess the number' \n"
          " - d 'Dragon cave' \n"
          " - c 'Coin flip' \n"
          " - h 'Hangman' \n"
          " - e to exit the program")

    choice = str(input())

    match choice:
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
        case _:
            print("Please, use built-in options!")


if __name__ == '__main__':
    welcome()
