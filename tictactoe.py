import random


def welcome():
    print("Welcome to the 'Tic Tac Toe'!")
    draw_board()


def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_sign():
    sign = ''

    while not (sign == 'X' or sign == 'O'):
        print('Do you want to be X or O?')
        sign = input().upper()

    match sign:
        case 'X':
            return ['X', 'O']
        case 'O':
            return ['O', 'X']


if __name__ == '__main__':
    welcome()
