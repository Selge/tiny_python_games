import random

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
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

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


def play_again():
    print("Wanna play again? (y/n)")
    player_answer = input().lower()
    match player_answer:
        case 'y':
            hangman()
        case 'n':
            print("Well, good luck next time!")
            exit()


def hangman():
    print("'H A N G M A N'")
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_is_over = False

    while True:
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
            play_again()


if __name__ == '__main__':
    hangman()
