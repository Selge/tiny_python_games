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


def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    coordinates = '1 2 3 4 5 6 7 8 9'.split()
    move = ' '
    while move not in coordinates or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)





if __name__ == '__main__':
    welcome()
