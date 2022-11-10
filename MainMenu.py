import os

games = {
    'c': os.system("coin_flip.py"),
    'd': os.system("dragon_cave.py"),
    'g': os.system("guess_the_number.py"),
    'e': exit(),
    'h': os.system("hangman.py")
}


def welcome():
    print("Welcome to the 'Tiny Python games shell'!\n"
          "Please, select a game from the list below:\n"
          " - g 'Guess the number' \n"
          " - d 'Dragon cave' \n"
          " - c 'Coin flip' \n"
          " - h 'Hangman'"
          " - e to exit the program")

    choice = str(input())

    for i in games:
        if choice == games[i]:
            games[i]
    else:
        print("Please, use built-in options!")
        welcome()


if __name__ == '__main__':
    welcome()
