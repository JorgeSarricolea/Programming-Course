# Create a program that simulates a game of hangman.
# The program should choose a random word from a list and allow the user to guess letters until they guess the word or run out of attempts.

import random

def hangman():
    words = ['python', 'java', 'ruby', 'php', 'javascript']
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()