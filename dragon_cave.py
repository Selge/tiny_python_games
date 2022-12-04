import random
import time

from MainMenu import welcome, play_again


def start():
    print("You're a travelling knight or a kind of treasure hunter in a land full of dragons.\n" 
          "You reached a mountain and in front of you, you see two caves:\n"
          "In one cave, the dragon is friendly and will share his treasure with you.\n" 
          "The other dragon is greedy and hungry, and will eat you on sight.\n")

    check_cave()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (press '1' or '2')")
        cave = str(input())

    return cave


def check_cave():
    choose_cave()
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(1)
    print("And so stinky.")
    time.sleep(3)
    print("Wait, oh shi... A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if choose_cave == str(friendly_cave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

    play_again(check_cave())


if __name__ == '__main__':
    welcome("Welcome to the 'Dragon cave'!")
