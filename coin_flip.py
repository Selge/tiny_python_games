import time
from random import choice

from MainMenu import welcome, play_again


coin = ['head', 'tail']


def start():
    print("What do you expect?\n"
          "- I want to flip a coin once (tap '1')"
          "- I want to play a flip coin game (tap '2')")

    start_choice = str(input())
    match start_choice:
        case '1':
            flip_coin_once()
        case '2':
            flip_coin_game()
        case _:
            print("Please, use built-in options!")
            start()


def flip_coin_once():
    print("Press 'Enter' to flip your coin")
    input()
    print("Tossing a coin...")
    time.sleep(3)

    flipped_coin = choice(coin)
    match flipped_coin:
        case 'head':
            print("Came up heads.")
        case 'tail':
            print("Came up tails.")

    play_again(start())


def flip_coin_game():
    print("What do you prefer: heads or tails?\n"
          "Type 'h' for 'heads' and 't' for 'tails'.")
    player_answer = str(input())
    print("How many times would you like to flip a coin? Print a number: ")
    coin_order = int(input())
    match player_answer:
        case 'h':
            coin_flipper(coin_order, 'head')
        case 't':
            coin_flipper(coin_order, 'tail')
        case _:
            print("Please, use built-in options!")
            flip_coin_game()

    play_again(start())


def coin_flipper(coin_order, coin_side):
    print(f"Well, I will flip a coin {coin_order} times. Guess how many times it will come up {coin_side}s.\n")
    flipped_coin = choice(coin)
    print("Tossing a coin...")
    time.sleep(3)

    heads = 0
    tails = 0
    flips = 0

    match coin_side:
        case 'head':
            while flips < coin_order:
                if flipped_coin == 'head':
                    heads = heads + 1
                flips = flips + 1
                result = heads
        case 'tail':
            while flips < coin_order:
                if flipped_coin == 'tail':
                    tails = tails + 1
                flips = flips + 1
                result = tails

    print(f"Well, ready to tell me how many times it will come up {coin_side}?\n"
          "Type a number: ")
    player_guess = int(input())

    if player_guess > result:
        print(f"That was too much. Out of {coin_order} coin tosses there have been {result} {coin_side}s.")
    elif player_guess < result:
        print(f"That was too few. Out of {coin_order} coin tosses there have been {result} {coin_side}s.")
    elif player_guess == result:
        print(f"Great! There have been indeed {result} {coin_side}s.")


if __name__ == '__main__':
    welcome("Welcome to the 'Coin Flip'!")
