import random
import sys

def init_board():
    matrix = []
    width_list = []
    for i in range(3):
        width_list.append('.')
    for unit in range(3):
        matrix.append(width_list)
    return matrix


def get_move():
    try:
        user_input = input('Please enter a coordinate (eg. A3): ')
        listed_coordinate = list(user_input)
    except ValueError as err:
        print({err})
    else:
        if listed_coordinate[0] == 'A':
            move1 = 1
        elif listed_coordinate[0] == 'B':
            move1= 3
        elif listed_coordinate[0] == 'C':
            move1 = 5
        if listed_coordinate[1] == '1':
            move2 = 1
        elif listed_coordinate[1] == '2':
            move2 = 3
        elif listed_coordinate[1] == '3':
            move2 = 5
        coordinate_tuple = (move1, move2)
        return coordinate_tuple

# get_move()

def mark(board, player_input, player_turn, mode = None):
    if player_turn % 2 == 1:
        if board[player_input[0]][player_input[1]] == ' . ':
            board[player_input[0]][player_input[1]] = ' X '
    else: 
        if board[player_input[0]][player_input[1]] == ' . ':
            board[player_input[0]][player_input[1]] = ' O '

def is_full(game_board):
    f = []
    for row in game_board:
        for item in row:
            f.append(item)
    if all(item != ' . ' for item in f) == True:
        return True
    else:
        return False



def print_board():
    board = []
    first_row = [' ', ' 1 ', ' ', ' 2 ', ' ',' 3 ']
    second_row = ['A', ' . ', '|', ' . ', '|', ' . ']
    third_row = [' ', '---', '+', '---', '+', '---']
    fourth_row = ['B', ' . ', '|', ' . ', '|', ' . ']
    fifth_row = [' ', '---', '+', '---', '+', '---']
    sixth_row = ['C', ' . ', '|', ' . ', '|', ' . ']
    board.append(first_row)
    board.append(second_row)
    board.append(third_row)
    board.append(fourth_row)
    board.append(fifth_row)
    board.append(sixth_row)
    return board

def printer(board):
    for row in board:
        print(''.join(row), end='\n')

def has_won(game_board):
    if game_board[1][1] == ' X ' and game_board[1][3] == ' X ' and game_board[1][5] == ' X ' or game_board[1][1] == ' O ' and game_board[1][3] == ' O ' and game_board[1][5] == ' O ':
        return True
    elif game_board[3][1] == ' X ' and game_board[3][3] == ' X ' and game_board[3][5] == ' X ' or game_board[3][1] == ' O ' and game_board[3][3] == ' O ' and game_board[3][5] == ' O ':
        return True
    elif game_board[5][1] == ' X ' and game_board[5][3] == ' X ' and game_board[5][5] == ' X ' or game_board[5][1] == ' O ' and game_board[5][3] == ' O ' and game_board[5][5] == ' O ':
        return True
    elif game_board[1][1] == ' X ' and game_board[3][1] == ' X ' and game_board[5][1] == ' X ' or game_board[1][1] == ' O ' and game_board[3][1] == ' O ' and game_board[5][1] == ' O ':
        return True
    elif game_board[1][1] == ' X ' and game_board[3][1] == ' X ' and game_board[5][1] == ' X ' or game_board[1][1] == ' O ' and game_board[3][1] == ' O ' and game_board[5][1] == ' O ':
        return True
    elif game_board[1][3]== ' X ' and game_board[3][3] == ' X ' and game_board[5][3] == ' X ' or game_board[1][3] == ' O ' and game_board[3][3] == ' O ' and game_board[5][3] == ' O ':
        return True
    elif game_board[1][5]== ' X ' and game_board[3][5] == ' X ' and game_board[5][5] == ' X ' or game_board[1][5] == ' O ' and game_board[3][5] == ' O ' and game_board[5][5] == ' O ':
        return True
    elif game_board[1][1]== ' X ' and game_board[3][3] == ' X ' and game_board[5][5] == ' X ' or game_board[1][1] == ' O ' and game_board[3][3] == ' O ' and game_board[5][5] == ' O ':
        return True
    elif game_board[1][3]== ' X ' and game_board[3][3] == ' X ' and game_board[5][1] == ' X ' or game_board[1][3] == ' O ' and game_board[3][3] == ' O ' and game_board[5][1] == ' O ':
        return True
    else:
        return False

def print_result(player_turn):
    if player_turn % 2 == 1:
        print('X has won!')
    else:
        print('O has won!')

def get_ai_move(matrix): #AI picks a random slot
    moves = [(1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5)]
    f = []
    for pair in moves:
        if matrix[pair[0]][pair[1]] == ' . ':
            f.append(pair)
    return f[random.randint(0,len(f)-1)]

def check_quit(inp):
    if inp == 'quit':
        sys.exit(0)

def tictactoe_game(mode = None):
    play_game = True
    turn = 0
    init = 0
    while play_game == True:
        while init == 0:
            init = init + 1
            board = print_board()
            printer(board)
            break
        turn += 1
        if mode == 'HUMAN-AI':
            if turn % 2 == 1:
                user_input = get_move()
                check_quit(user_input)
                mark(board, user_input, turn)
            else:
                ai_move = get_ai_move(board)
                mark(board, ai_move, turn)
        elif mode == 'AI-HUMAN':
            if turn % 2 == 0:
                user_input = get_move()
                check_quit(user_input)
                mark(board, user_input, turn)
            else:
                ai_move = get_ai_move(board)
                mark(board, ai_move, turn)  
        else: 
            user_input = get_move()
            check_quit(user_input)
            mark(board, user_input, turn)

        printer(board)
        verdict = has_won(board)
        if verdict == True:
            print_result(turn)
            play_game = False
            break
        full_board = is_full(board)
        if full_board == True:
            print('It\'s a tie!')
            play_game = False
        


def main_menu():
    print('Welcome to TIC-TAC-TOE!')
    choice = input('Please choose a game mode (1. Human vs. Human 2. Human vs AI 3. AI vs Human): ')
    if choice == '1':
        tictactoe_game()
    elif choice == '2':
        tictactoe_game('HUMAN-AI')
    else:
        tictactoe_game('AI-HUMAN')


def main():
    main_menu()
    # tictactoe_game('AI-HUMAN')


if __name__ == '__main__':
    main()

