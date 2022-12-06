import random

from MainMenu import welcome, play_again

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

