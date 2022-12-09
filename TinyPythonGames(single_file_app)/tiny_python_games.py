import os
import math
import random
import sys
import time

from random import choice


class TinyPythonGames:
    def __init__(self):
        self.player_name = None
        self.menu()
        self.wanna_play(self.player_name)
        self.game_menu()
        self.welcome()
        self.play_again()
        
    def menu(self):
        print("Welcome to the 'Tiny Python games'!\nPlease,type in your name: ")
        self.player_name = input()
        wanna_play(self.player_name)


    def wanna_play(player_name):
        print(f"Well, {player_name}, wanna play a little bit? y/n?")
        player_answer = str(input())
        match player_answer:
            case "y":
                game_menu()
            case "n":
                print("Well, see ya later! Bye!")
                exit()
            case _:
                print("Please, use built-in options!")
                wanna_play(player_name)


    def game_menu():
        print("Welcome to the 'Tiny Python games shell'!\n"
              "Please, select a game from the list below:\n"
              " - a 'Dodger' \n"
              " - b 'Bagels' \n"
              " - c 'Coin flip' \n"
              " - d 'Dragon cave' \n"
              " - g 'Guess the number' \n"        
              " - h 'Hangman' \n"
              " - r 'Reversi' \n"
              " - s 'Sonar Treasure Hunt' \n"
              " - t 'Tic Tac Toe' \n"
              " - e to exit the program")

        choice = str(input())

        match choice:
            case 'a':
                pass
            case 'b':
                Bagels()
            case 'c':
                CoinFlip()
            case 'd':
                DragonCave()
            case 'g':
                GuessTheNumber()
            case 'e':
                exit()
            case 'h':
                Hangman()
            case 'r':
                pass
            case 's':
                SonarTreasureHunt()
            case 't':
                TicTacToe()
            case _:
                print("Please, use built-in options!")


    def welcome(game_name: str, file_game):
        print(game_name)
        time.sleep(2)
        file_game()


    def play_again(game):
        print("Wanna play again? (y/n)\n"
              "Or type in 'm' to get back to the main menu")
        player_answer = input().lower()
        match player_answer:
            case 'y':
                game()
            case 'n':
                print("Well, good luck next time!")
                exit()
            case "m":
                game_menu()
            case _:
                exit()


class Bagels:
    def __init__(self):
        pass

    def get_secret_num(NUM_DIGITS):
        numbers = list(range(10))
        random.shuffle(numbers)
        secret_num = ''
        for i in range(NUM_DIGITS):
            secret_num += str(numbers[i])
        return secret_num

    def get_clues(guess, secret_num):
        if guess == secret_num:
            return "You got it!"

        clues = []
        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                clues.append("Fermi")
            elif guess[i] in secret_num:
                clues.append("Pico")

        if len(clues) == 0:
            return "Bagels"

        clues.sort()
        return ' '.join(clues)

    def is_only_digits(num):
        if num == '':
            return False

        for i in num:
            if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                return False
        return True

    def prompt(NUM_DIGITS):
        print(f"I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.")
        time.sleep(2)
        print("Here are some clues:\n"
              "When I say:      That means:\n"
              " 'Pico'          One digit is correct but in the wrong position.\n"
              " 'Fermi'         One digit is correct and in the right position.\n"
              " 'Bagels'        No digit is correct.\n"
              f"Please, note that each your guess must be a {NUM_DIGITS}-digit number,\n"
              "otherwise the guess will not work out.")

    def difficulty():
        NUM_DIGITS = 0
        MAX_GUESS = 0
        iq_levels = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}
        difficulty = 'X'
        while difficulty not in iq_levels.keys():
            print('Enter difficulty: E - Easy, M - Medium, H - Hard')
            difficulty = input().upper()
            match difficulty:
                case 'E':
                    NUM_DIGITS = 3
                    MAX_GUESS = 10
                case 'M':
                    NUM_DIGITS = 4
                    MAX_GUESS = 8
                case 'H':
                    NUM_DIGITS = 5
                    MAX_GUESS = 5

            return NUM_DIGITS, MAX_GUESS

    def pico_fermi_bagels():
        NUM_DIGITS, MAX_GUESS = difficulty()
        prompt(NUM_DIGITS)
        while True:
            secret_num = get_secret_num(NUM_DIGITS)
            print(f"I have thought up a number. You have {MAX_GUESS} guesses to get it.")

            guesses_taken = 1
            while guesses_taken <= MAX_GUESS:
                guess = ''
                while len(guess) != NUM_DIGITS or not is_only_digits(guess):
                    print(f"Guess #{guesses_taken}: ")
                    guess = input()

                print(get_clues(guess, secret_num))
                guesses_taken += 1

                if guess == secret_num:
                    break
                if guesses_taken > MAX_GUESS:
                    print(f"You ran out of guesses. The answer was {secret_num}.")

            play_again(pico_fermi_bagels)


class CoinFlip:
    def __init__(self):
        pass

    coin = ['head', 'tail']

    def coin_flip():
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
                coin_flip()

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

        play_again(coin_flip)

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

        play_again(coin_flip)

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


class DragonCave:
    def __init__(self):
        pass

    def dragon_cave():
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

        play_again(check_cave)


class GuessTheNumber:
    def __init__(self):
        pass

    def guess_the_number():
        print("Please choose target difficulty level. Type in:\n"
              " - 'a' to guess a number between 0 and 10\n"
              " - 'b' to guess a number between 0 and 100\n"
              " - 'c' to guess a number between 0 and 1000\n"
              " - 'e' if you've changed your mind and wanna get out of here")
        player_answer = str(input())
        match player_answer:
            case "a":
                game_a()
            case "b":
                game_b()
            case "c":
                game_c()
            case "e":
                print("Well, see ya later! Bye!")
                exit()
            case _:
                print("Please, use built-in options!")
                guess_the_number()

    def game_a():
        number_a = random.randint(0, 10)
        range_guess = range(6)
        print("I am thinking of a number between 0 and 10. Can you guess?")
        guess(number_a, range_guess)

    def game_b():
        number_b = random.randint(0, 100)
        range_guess = range(11)
        print("I am thinking of a number between 0 and 100. Can you guess?")
        guess(number_b, range_guess)

    def game_c():
        number_c = random.randint(0, 1000)
        range_guess = range(21)
        print("I am thinking of a number between 0 and 1000. Can you guess?")
        guess(number_c, range_guess)

    def guess(number, range_guess):
        digits_taken = 0
        for digits_taken in range_guess:
            print("Your guess: ")
            player_guess = int(input())
            if player_guess < number:
                print("Your digit is too small.")
            elif player_guess > number:
                print("That's too big.")
            elif player_guess == number:
                break
        if player_guess == number:
            digits_taken = str(digits_taken + 1)
            print(f"Great! You've passed in {digits_taken} guesses.")
            play_again(guess_the_number)
        elif player_guess != number:
            number_guess = str(number)
            print(f"Alas. The number was: {number_guess}")
            play_again(guess_the_number)


class Hangman:
    def __init__(self):
        pass

    HANGMAN_PICS = ['''
        +---+
            |
            |
            |
            |
            |
        =========
    ''', '''
        +---+
        |   |
            |
            |
            |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
            |
            |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
        |   |
            |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
       /|   |
            |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
       /|\  |
            |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
       /|\  |
       /    |
            |
        =========
    ''', '''
        +---+
        |   |
        0   |
       /|\  |
       / \  |
            |
        =========
    ''', '''
        +---+
        |   |
       [0   |
       /|\  |
       / \  |
            |
        =========
    ''', '''
        +---+
        |   |
       [0]  |
       /|\  |
       / \  |
            |
        =========
    ''']

    ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'

    words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
             'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon heptagon octagon'.split(),
             'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
             'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

    iq_levels = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}

    def get_random_word(word_dict):
        word_key = random.choice(list(word_dict.keys()))
        word_index = random.randint(0, len(word_dict[word_key]) - 1)
        return [word_dict[word_key][word_index], word_key]

    def display_board(missed_letters, correct_letters, secret_word):
        print(HANGMAN_PICS[len(missed_letters)])
        print()

        print('Missed letters:', end=' ')
        for letter in missed_letters:
            print(letter, end=' ')
        print()

        blanks = '_' * len(secret_word)

        for i in range(len(secret_word)):
            if secret_word[i] in correct_letters:
                blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

        for letter in blanks:
            print(letter, end=' ')
        print()

    def get_guess(already_guessed):
        while True:
            print("Please, guess a letter")
            guess = input().lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif guess in already_guessed:
                print("You have already guessed that letter. Choose again.")
            elif guess not in ABC_ENG:
                print("Please enter a LETTER.")
            else:
                return guess

    def hangman():
        print("'H A N G M A N'")

        difficulty = 'X'
        while difficulty not in iq_levels.keys():
            print('Enter difficulty: E - Easy, M - Medium, H - Hard')
            difficulty = input().upper()
            match difficulty:
                case 'M':
                    del HANGMAN_PICS[8]
                    del HANGMAN_PICS[7]
                case 'H':
                    del HANGMAN_PICS[8]
                    del HANGMAN_PICS[7]
                    del HANGMAN_PICS[5]
                    del HANGMAN_PICS[3]

        missed_letters = ''
        correct_letters = ''
        secret_word, secret_set = get_random_word(words)
        game_is_over = False

        while True:
            print('The secret word is in the set: ' + secret_set)
            display_board(missed_letters, correct_letters, secret_word)

            guess = get_guess(missed_letters + correct_letters)
            if guess in secret_word:
                correct_letters = correct_letters + guess

                found_all_letters = True
                for i in range(len(secret_word)):
                    if secret_word[i] not in correct_letters:
                        found_all_letters = False
                        break
                if found_all_letters:
                    print(f"Yes! The secret word is '{secret_word}'! You have won!")

                    game_is_over = True
            else:
                missed_letters = missed_letters + guess

                if len(missed_letters) == len(HANGMAN_PICS) - 1:
                    display_board(missed_letters, correct_letters, secret_word)
                    print(f"You have run out of guesses!\nAfter {str(len(missed_letters))} missed guesses and"
                          f"{str(len(correct_letters))} correct guesses, the word was'{secret_word}'.")

                    game_is_over = True

            if game_is_over:
                play_again(hangman)


class TicTacToe:
    def __init__(self):
        pass

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

        if sign == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def first_step():
        if random.randint(0, 1) == 0:
            return 'Computer'
        else:
            return 'Human'

    def make_move(board, sign, move):
        board[move] = sign

    def is_winner(board, sign):
        return ((board[1] == sign and board[2] == sign and board[3] == sign) or
                (board[4] == sign and board[5] == sign and board[6] == sign) or
                (board[7] == sign and board[8] == sign and board[9] == sign) or
                (board[1] == sign and board[4] == sign and board[7] == sign) or
                (board[2] == sign and board[5] == sign and board[8] == sign) or
                (board[3] == sign and board[6] == sign and board[9] == sign) or
                (board[1] == sign and board[5] == sign and board[9] == sign) or
                (board[3] == sign and board[5] == sign and board[7] == sign))

    def get_board_copy(board):
        board_copy = []
        for i in board:
            board_copy.append(i)
        return board_copy

    def is_space_free(board, move):
        return board[move] == ' '

    def get_player_move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
            print("What's your next move? (1-9)")
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

            play_again(tic_tac_toe_game)


class SonarTreasureHunt:
    def __init__(self):
        pass

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

        print(tens_digits_line)
        print(' ' + ('01234567890' * 6))
        print()

        for row in range(15):
            if row < 10:
                extra_space = ' '
            else:
                extra_space = ''

            board_row = ''
            for column in range(60):
                board_row += board[column][row]

            print(f"{extra_space}{row} {board_row} {row}")

        print()
        print(' ' + ('01234567890' * 6))
        print(tens_digits_line)

    def get_random_chests(num_chests):
        chests = []
        while len(chests) < num_chests:
            new_chest = [random.randint(0, 59), random.randint(0, 14)]
            if new_chest not in chests:
                chests.append(new_chest)

        return chests

    def is_on_board(x, y):
        return x >= 0 and x <= 59 and y >= 0 and y <= 14

    def make_move(board, chests, x, y):
        smallest_distance = 100
        for cx, cy in chests:
            distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

            if distance < smallest_distance:
                smallest_distance = distance

            if smallest_distance == 0:
                chests.remove([x, y])
                return "You have found a sunken treasure chest!"
            else:
                if smallest_distance < 10:
                    board[x][y] = str(smallest_distance)
                    return f"Treasure detected at a distance of {smallest_distance} from the sonar device."
                else:
                    board[x][y] = 'X'
                    return "Sonar did not detect anything. All treasure chests out of range."

    def enter_player_move(previous_moves):
        print("Where do you want to drop the next sonar device? (0-59 0-14)(or type 'e' to quit)")
        while True:
            move = input()
            if move.lower == 'e':
                print('Thanks for playing!')
                sys.exit()

            move = move.split()
            if len(move) == 2 and move[0].isdigit() and is_on_board(int(move[0]), int(move[1])):
                if [int(move[0]), int(move[1])] in previous_moves:
                    print("You already checked there.")
                    continue
                return [int(move[0]), int(move[1])]

            print("Enter a number from 0 to 59, a space, then a number from 0 to 14.")

    def show_instructions():
        print("""Instructions:
    You are the captain of the 'Lorelei', a treasure-hunting ship. 
    Your current mission is to use sonar devices to find three sunken treasure chests at the bottom of the ocean. 
    But you only have cheap sonar that finds distance, not direction...

    Enter the coordinates to drop a sonar device. The ocean map will be marked with how far away the nearest chest is, 
    or an X if it is beyond the sonar device's range. 
    E.g., the 'C' ('chests') marks are where chests are. 
    The sonar device shows a '3' mark because the closest chest is 3 spaces away:
                              1         2         3
                    012345678901234567890123456789012

                  0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                  1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                  2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
                  3 ````````~~~`````~~~`~`````~`~``~` 3
                  4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                    012345678901234567890123456789012
                              1         2         3
        (In the real game, the chests are not visible in the ocean.)
    """)

        input("Push 'enter' to proceed...")

        print("""
    When you drop a sonar device directly on a chest, you retrieve it and the other sonar devices update 
    to show how far away the next nearest chest is. The chests are beyond the range of the sonar device on the left, 
    so it shows an 'X' mark.
                                  1         2         3
                        012345678901234567890123456789012

                      0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                      1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                      2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
                      3 ````````~~~`````~~~`~`````~`~``~` 3
                      4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                        012345678901234567890123456789012
                                  1         2         3
    The treasure chests don't move around. Sonar devices can detect treasure chests up to a distance of 9 spaces. 
    Try to collect all 3 chests before running out of sonar devices. 
    Good luck!
    """)

        input("Push 'enter' to start the game.")
        sonar_treasure_hunt()

    def instructions():
        question = str(input("Would you like to view the instructions? (y/n)")).lower()
        match question:
            case 'y':
                show_instructions()
            case 'n':
                sonar_treasure_hunt()
            case _:
                print("Please, use built-in options!")
                instructions()

    def sonar_treasure_start():
        print("S O N A R")
        instructions()

    def sonar_treasure_hunt():
        while True:
            sonar_devices = 20
            the_board = get_new_board()
            the_chests = get_random_chests(3)
            draw_board(the_board)
            previous_moves = []

            while sonar_devices > 0:
                print(f"You have {sonar_devices} sonar device(s) left. {len(the_chests)} treasure chest(s) remaining.")

                x, y = enter_player_move(previous_moves)
                previous_moves.append([x, y])

                move_result = make_move(the_board, the_chests, x, y)
                if move_result == False:
                    continue
                else:
                    if move_result == "You have found a sunken treasure chest!":
                        for x, y in previous_moves:
                            make_move(the_board, the_chests, x, y)
                        draw_board(the_board)
                        print(move_result)

                if len(the_chests) == 0:
                    print("You have found all the sunken treasure chests! Congratulations and good game!")
                    play_again(sonar_treasure_start)

                sonar_devices -= 1

            if sonar_devices == 0:
                print("""
                We've run out of sonar devices! Now we have to turn the ship around and head for home 
                with treasure chests still out there! Game over.
                """)
                print(f"The remaining chests were here: ")
                for x, y in the_chests:
                    print(f"{x}, {y}")
                play_again(sonar_treasure_start)


if __name__ == '__main__':
    TinyPythonGames.menu()
