import os


def welcome():
    print("Welcome to the 'Tiny Python games shell'!\n"
          "Please, select a game from the list below:\n"
          " - a 'Guess the number' \n"
          " - b 'Dragon cave' \n"
          " - c 'Coin flip' \n"
          " - e to exit the program")

    choice = str(input())

    if choice == 'a':
        os.system("guess_the_number.py")
    elif choice == 'b':
        os.system("dragon_cave.py")
    elif choice == 'c':
        os.system("coin_flip.py")
    elif choice == 'e':
        exit()
    else:
        print("Please, use built-in options!")
        welcome()


if __name__ == '__main__':
    welcome()
