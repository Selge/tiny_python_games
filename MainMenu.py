import os


def welcome():
    print("Welcome to the 'Tiny Python games shell'!\n"
          "Please, select a game from the list below:\n"
          " - g 'Guess the number' \n"
          " - d 'Dragon cave' \n"
          " - c 'Coin flip' \n"
          " - h 'Hangman'"
          " - e to exit the program")

    choice = str(input())

    if choice == 'g':
        os.system("guess_the_number.py")
    elif choice == 'd':
        os.system("dragon_cave.py")
    elif choice == 'c':
        os.system("coin_flip.py")
    elif choice == 'h':
        os.system("hangman.py")
    elif choice == 'e':
        exit()
    else:
        print("Please, use built-in options!")
        welcome()


if __name__ == '__main__':
    welcome()
