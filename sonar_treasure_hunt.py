import random
import sys
import math

from MainMenu import welcome, play_again


def get_new_board():
    board = []
    for x in range(60):
        board.append([])
    for y in range(15):
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
        return board


def draw_board(board):
    tens_digits_line = ' '
    for i in range(1, 6):
        tens_digits_line += (' ' * 9) + str(i)



if __name__ == '__main__':
    welcome("Welcome to the 'Hangman'!", sonar_treasure_hunt)
