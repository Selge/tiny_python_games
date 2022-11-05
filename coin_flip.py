import random
import time


def start():
    print("Welcome to the 'Coin flip'!\n"
          "What do you expect?\n"
          "- I want to flip a coin once (tap '1')"
          "- I want to play a flip coin game (tap '2')")

    start_choice = str(input())
    if start_choice == '1':
        flip_coin()
    elif start_choice == '2':
        flip_coin_game()
    else:
        print("Please, use built-in options!")
        start()


def flip_coin():
    print("Press 'Enter' to flip your coin")
    input()
    print("Tossing a coin...")
    time.sleep(3)

    flipped_coin = random.randint(0, 1)
    if flipped_coin == 0:
        print("Came up heads.")
    elif flipped_coin == 1:
        print("Came up tails.")

    print("Wanna try again? y/n\n"
          "Or type in 'm' to get back to the main menu")
    player_answer = str(input())
    if player_answer == "y":
        flip_coin()
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    elif player_answer == "m":
        start()
    else:
        exit()


def flip_coin_game():
    print("What do you prefer: heads or tails?\n"
          "Type 'h' for 'heads' and 't' for 'tails'.")
    player_answer = str(input())
    print("How many times would you like to flip a coin? Print a number: ")
    coin_order = int(input())

    if player_answer == 'h':

        print(f"Well, I will flip a coin {coin_order} times. Guess how many times it will come up heads.\n")
        flipped_coin = random.randint(0, 1)
        print("Tossing a coin...")
        time.sleep(3)

        heads = 0
        flips = 0
        while flips < coin_order:
            if flipped_coin == 0:
                heads = heads + 1
            flips = flips + 1

        print("Well, ready to tell me how many times it will come up heads?\n"
              "Type a number: ")
        player_guess = int(input())

        if player_guess > heads:
            print(f"That was too big. Out of {coin_order} coin tosses there have been {heads} heads")
        elif player_guess < heads:
            print(f"That was too few. Out of {coin_order} coin tosses there have been {heads} heads")
        elif player_guess == heads:
            print(f"Great! There have been indeed {heads} heads.")

    elif player_answer == 't':
        print(f"Well, I will flip a coin {coin_order} times. Guess how many times it will come up tails.\n")
        flipped_coin = random.randint(0, 1)
        print("Tossing a coin...")
        time.sleep(3)

        tails = 0
        flips = 0
        while flips < coin_order:
            if flipped_coin == 1:
                tails = tails + 1
            flips = flips + 1

        print("Well, ready to tell me how many times it will come up tails?\n"
              "Type a number: ")
        player_guess = int(input())

        if player_guess > tails:
            print(f"That was too big. Out of {coin_order} coin tosses there have been {tails} tails")
        elif player_guess < tails:
            print(f"That was too few. Out of {coin_order} coin tosses there have been {tails} tails")
        elif player_guess == tails:
            print(f"Great! There have been indeed {tails} tails.")

    else:
        print("Please, use built-in options!")
        flip_coin_game()

    print("Wanna try again? y/n\n"
          "Or type in 'm' to get back to the main menu")
    player_answer = str(input())
    if player_answer == "y":
        flip_coin_game()
    elif player_answer == "n":
        print("Well, see ya later! Bye!")
        exit()
    elif player_answer == "m":
        start()
    else:
        exit()


if __name__ == '__main__':
    start()
