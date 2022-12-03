import random


def welcome():
    print("Welcome to the 'Tic Tac Toe'!")
    tic_tac_toe_game()


def draw_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


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

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_sign):
    even_moves = [2, 4, 6, 8]
    odd_moves = [1, 3, 7, 9]

    if computer_sign == 'X':
        player_sign = 'O'
    else:
        player_sign = 'X'

    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_sign, i)
            if is_winner(board_copy, computer_sign):
                return i

    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_sign, i)
            if is_winner(board_copy, player_sign):
                return i

    move = choose_random_move_from_list(board, odd_moves)
    if move != None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, even_moves)


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def tic_tac_toe_game():
    while True:
        the_board = [' '] * 10
        player_sign, computer_sign = input_player_sign()
        turn = first_step()
        print(f'The {turn} will go first.')
        game_is_active = True

        while game_is_active:
            if turn == 'Human':
                draw_board(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_sign, move)

                if is_winner(the_board, player_sign):
                    draw_board(the_board)
                    print('Congrats! You have won the game!')
                    game_is_active = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Computer'

            else:
                move = get_computer_move(the_board, computer_sign)
                make_move(the_board, computer_sign, move)

                if is_winner(the_board, player_sign):
                    draw_board(the_board)
                    print('The computer has beaten you! You lose.')
                    game_is_active = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Human'


def play_again():
    print("Wanna play again? (y/n)")
    player_answer = input().lower()
    match player_answer:
        case 'y':
            tic_tac_toe_game()
        case 'n':
            print("Well, good luck next time!")
            exit()


if __name__ == '__main__':
    welcome()
