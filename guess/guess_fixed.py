import os
import sys

from random import choice
from string import ascii_lowercase


FILENAME = 'sowpods.txt'
work_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(work_directory)


def get_random_word(file_path):
    with open(file_path, 'r') as words_file:
        random_words = [word for word in words_file]
        random_word = choice(random_words)
        prepared_random_word = random_word.strip().lower()

    return prepared_random_word


def get_user_input_letter(attempt_count, letter_guesses):
    user_input_template = f'> Guess a letter ({attempt_count} attempt_counts left): '
    raw_user_input = input(user_input_template)
    user_input = raw_user_input.lower()

    if len(user_input) != 1 or user_input not in ascii_lowercase:
        print("> Please input a letter!")
    elif user_input in letter_guesses:
        print(f"> You have guessesed '{user_input}' before")
    else:
        return user_input


def encrypt_word(word):
    encrypted_word_letters = []
    for letter in word:
        letter = None if letter != ' ' else letter
        encrypted_word_letters.append(letter)

    return encrypted_word_letters


def decrypt_word(encrypted_word_letters):
    decrypted_word_letters = []
    for letter in encrypted_word_letters:
        letter = ' ' if letter is None else letter
        decrypted_word_letters.append(letter)

    return decrypted_word_letters


def display_game_interface(game_parameters):
    quest_word = game_parameters['quest_word']
    encrypted_word_letters = game_parameters['encrypted_word_letters']
    wrong_letter_guesses = game_parameters['wrong_letter_guesses']

    wrong_letter_guesses = ', '.join(wrong_letter_guesses)

    decrypted_word_letters = decrypt_word(encrypted_word_letters)
    decrypted_word = ' '.join(decrypted_word_letters)

    encrypted_word_dummy_letters = ['-' if letter != ' ' else ' ' for letter in encrypted_word_letters]
    encrypted_word_dummy = ' '.join(encrypted_word_dummy_letters)

    game_interface_template = f'\nWrong guess: {wrong_letter_guesses}\n{decrypted_word}\n{encrypted_word_dummy}'
    print(game_interface_template)


def check_user_guess(game_parameters, user_letter):
    quest_word = game_parameters['quest_word']

    if user_letter is not None:
        for index in range(len(quest_word)):
            if user_letter == quest_word[index]:
                game_parameters['encrypted_word_letters'][index] = user_letter
        game_parameters['letter_guesses'].append(user_letter)
        if user_letter not in game_parameters['encrypted_word_letters']:
            game_parameters['wrong_letter_guesses'].append(user_letter)
            game_parameters['attempt_count'] -= 1

    return game_parameters


def check_game_status(game_parameters):
    if None not in game_parameters['encrypted_word_letters']:
        display_game_interface(game_parameters)
        sys.exit('> You win!')
    elif game_parameters['attempt_count'] == 0:
        display_game_interface(game_parameters)
        sys.exit(f"> You lose...\n> Answer: {game_parameters['quest_word'].capitalize()}")


def start_game(quest_word):
    game_parameters = {
        'quest_word': quest_word,
        'attempt_count': 6,
        'encrypted_word_letters': encrypt_word(quest_word),
        'letter_guesses': [],
        'wrong_letter_guesses': []
    }

    while game_parameters['attempt_count'] >= 0:
        check_game_status(game_parameters)
        display_game_interface(game_parameters)
        user_input_letter = get_user_input_letter(game_parameters['attempt_count'],
                                                  game_parameters['letter_guesses'])
        game_parameters = check_user_guess(game_parameters, user_input_letter)


if __name__ == "__main__":
    words_file_path = os.path.join('media', FILENAME)
    random_word = get_random_word(words_file_path)
    start_game(random_word)
