import random

path = '/home/bogdan/Desktop/projects/practice/'
file_name = 'word_list.txt'


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

# 3 difficulty levels - easy 7 lives medium 5 lives hard 3 lives
# if difficulty == easy: lives = 7 etc...
def choose_word():
    with open(path + file_name, 'r') as file:
        words_list = file.readlines()
        # random_word = 
        random_word = words_list[random.randrange(0, len(words_list))]
        #pick a random word depending on the difficulty, hard difficulty may result in words with no duplicate letters ( use sets)
        # print(random_word)
        return random_word

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
    while play_game == True:
        while init == 0:
            print('Welcome to the Hangman game!')
            init += 1
            # lives = difficulty()
            # # hangman = display_hangman(lives)
            # word = choose_word()
            underscore = underscore_word(word)
        print(underscore)
        user_input = ask_input()

        if user_input == 'quit':
            print('Quitting game!')
            break

        for i in list(word.lower()):
            indexxx = list(word.lower()).index(i)
            if user_input == i:
                underscore[indexxx] = user_input
                print(underscore)
            for i in underscore:
                if user_input == i:
                    print('You\'ve already guessed this letter.')
        if user_input not in list(word.lower()):
            lives -= 1 
            print(display_hangman(-1)) # show first picture, first state of the hangman

        if lives == 0:
            print(display_hangman(0))
            print('You lost')
            break

        # for i in underscore:
        #     if i == '_' is False:
        #             print('you won')



def main():
    play(choose_word(), difficulty())


if __name__ == '__main__':
    main()





