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


def first_step():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Human'


def make_move(board, sign, move):
    board[move] = sign


def is_winner(board, sign):
    return ((board[7] == sign and board[8] == sign and board[9] == sign) or
            (board[4] == sign and board[5] == sign and board[6] == sign) or
            (board[1] == sign and board[2] == sign and board[3] == sign) or
            (board[7] == sign and board[4] == sign and board[1] == sign) or
            (board[8] == sign and board[5] == sign and board[2] == sign) or
            (board[9] == sign and board[6] == sign and board[3] == sign) or
            (board[7] == sign and board[5] == sign and board[3] == sign) or
            (board[9] == sign and board[5] == sign and board[1] == sign))


if __name__ == '__main__':
    welcome()
