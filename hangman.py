import random
import string

path = '/home/bogdan/Desktop/projects/practice/'
file_name = 'countries-and-capitals.txt'


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def choose_word():
    with open(path + file_name, 'r') as file:
        words_list = file.readlines()
        random_word = words_list[random.randrange(0, len(words_list))]
        listed_word = list(random_word)
        for elem in listed_word:
            half_index = listed_word.index(elem)
            if elem == '|':
                chosen_word = listed_word[:half_index]
        alphabet = list(string.ascii_letters)
        for item in chosen_word:
            if item not in alphabet:
                chosen_word.remove(item)

        # random_word = random_word[:-1] #because every words ends with '\n'
        #pick a random word depending on the difficulty, hard difficulty may result in words with no duplicate letters ( use sets)
        return ''.join(chosen_word)

def ask_input():
    letter = input('Please enter a leter: ')
    letter.lower() # for making the input case insensitive
    return letter

def difficulty():
    difficulty = int(input('Pick a difficulty level (1 - EASY 2 - MEDIUM 3 - HARD): '))
    if difficulty == 1:
        lives = 7
    elif difficulty == 2:
        lives = 5
    elif difficulty == 3: 
        lives = 3
    return lives

def underscore_word(word):
    show_underline = []
    for i in list(word):
        show_underline.append('_')
    return show_underline

def play(word,lives):
    init = 0
    play_game = True
    stance = -1 #shows the hangman stance
    while play_game == True:
        while init == 0:
            print('Welcome to the Hangman game!')
            init += 1
            underscore = underscore_word(word)
            print(' '.join(underscore))
            if lives == 7:
                difficulty_level = 1
            elif lives == 5:
                difficulty_level = 2
            else:
                difficulty_level = 3
        user_input = ask_input()

        if user_input == 'quit':
            print('Quitting game. Good-bye!!')
            play_game = False
        for item in underscore:
            if user_input == item:
                print('You\'ve already guessed this letter. Please enter a different one!')
                break
        indices = [idx for idx, value in enumerate(list(word.lower())) if value == user_input]
        for i in list(word.lower()):
            for idx in indices:
                if user_input == i:
                    underscore[idx] = user_input
        print(' '.join(underscore).capitalize())

        if user_input not in list(word.lower()):
            lives -= 1 
            if difficulty_level == 1:
                stance = stance - 1
            elif difficulty_level == 2:
                stance -= 2
            else:
                stance = stance - 2
            if stance <= - 7:
                print(display_hangman(0))
                print('You lost')
                play_game = False
            print(display_hangman(stance)) 

        if all(item != '_' for item in underscore) == True:
            print('You won!')
            print(word)
            play_game = False
        



def main():
    play(choose_word(), difficulty())
    # play('Codecool', 5)


if __name__ == '__main__':
    main()






