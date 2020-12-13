import string
import os
from copy import deepcopy 

alphabet = string.ascii_uppercase

ships_for_player1 = [2,1]
ships_for_player2 = [2,1]
REPRESENTATION_WATER_ON_MAP = '0'
REPRESENTATION_MISS_ON_MAP = 'M'
REPRESENTATION_SHIP_ON_MAP = 'X'
REPRESENTATION_HIT_ON_MAP = 'H'
REPRESENATATION_SUNK_ON_MAP = 'S'

def create_map():
    board = [[' ', '1', '2', '3', '4', '5'], ['A', '0', '0', '0', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', '0', '0', '0', '0']]
    return board

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') 

def coordinates_in_valid_format(coordinates):
    if list(coordinates)[0] in list(alphabet) and list(coordinates)[1].isdigit() and len(coordinates) == 2:
        return True
    else:
        print('Invalid input, coordinates are not in a valid format (e.g. A2)!')
        return False

def coordinate_are_inside_map(coordinates):
    list_of_coordinates = list(coordinates)
    f_index_alphabet = list(alphabet).index('F')
    if list_of_coordinates[0] in list(alphabet)[(f_index_alphabet + 1):len(alphabet)] or int(list_of_coordinates[1]) > 5:
        print('Coordinates are outside the range of the map!')
        return False
    else:
        return True

def transform_coordinates(coordinates):
    list_of_coordinates = list(coordinates)
    if list_of_coordinates[0] == 'A':
        x_axis_coordinate = 1
    elif list_of_coordinates[0] == 'B':
        x_axis_coordinate = 2
    elif list_of_coordinates[0] == 'C':
        x_axis_coordinate = 3
    elif list_of_coordinates[0] == 'D':
        x_axis_coordinate = 4
    elif list_of_coordinates[0] == 'E':
        x_axis_coordinate = 5
    y_axis_coordinate = int(list_of_coordinates[1])
    return [x_axis_coordinate, y_axis_coordinate]


def read_coordinates():
    while True:
        coordinates = input('Please enter coordinates in the form [letter][digit]: ')
        if coordinates_in_valid_format(coordinates):
            if coordinate_are_inside_map(coordinates):
                [x_axis, y_axis] = transform_coordinates(coordinates)
                return [x_axis, y_axis]



def mark_ship_on_map(board, ship, x_axis, y_axis):
    board[x_axis][y_axis] = REPRESENTATION_SHIP_ON_MAP

def display_game_map(board):
    for row in board:
        print(' '.join(row), end='\n')

def place_ships_on_map(ships):
    count = 0
    game_map = create_map()
    display_game_map(game_map)
    for ship in ships:
        count += 1
        print(f'Placing ship number {count}, which is {ship} cells long!')
        for unit in range(ship):
            [x_axis, y_axis] = read_coordinates()
            mark_ship_on_map(game_map, ship, x_axis, y_axis)
        display_game_map(game_map)
    return game_map



def display_current_player_turn(current_player_map, player_one_map):
    first_player = 'Player 1'
    second_player = 'Player 2'
    if current_player_map == player_one_map:
        print('Player 1 is shooting now!')
        return first_player
    else:
        print('Player 2 is shooting now!')
        return second_player


def ship_has_no_more_lives(board, x_axis, y_axis):
    try:
        if board[x_axis][y_axis + 1] != REPRESENTATION_SHIP_ON_MAP and board[x_axis][y_axis - 1] != REPRESENTATION_SHIP_ON_MAP:
            return True
        else:
            return False
    except IndexError:
        if y_axis == 5:
            if board[x_axis][y_axis - 1] == REPRESENTATION_WATER_ON_MAP or board[x_axis][y_axis - 1] == REPRESENTATION_MISS_ON_MAP:
                return True
        elif y_axis == 0:
            if board[x_axis][y_axis + 1] == REPRESENTATION_WATER_ON_MAP or board[x_axis][y_axis + 1] == REPRESENTATION_MISS_ON_MAP:
                return True



def mark_ship_as_dead(board, x_axis, y_axis):
    try:
        board[x_axis][y_axis] = REPRESENATATION_SUNK_ON_MAP
        if board[x_axis][y_axis + 1] == REPRESENTATION_HIT_ON_MAP:
            board[x_axis][y_axis + 1] = REPRESENATATION_SUNK_ON_MAP
        elif board[x_axis][y_axis - 1] == REPRESENTATION_HIT_ON_MAP:
            board[x_axis][y_axis - 1] = REPRESENATATION_SUNK_ON_MAP
        return board
    except IndexError as err:
        print(f'{err}')


def shoot_at_coordinates(game_map, x_axis, y_axis):
    if game_map[x_axis][y_axis] == REPRESENTATION_WATER_ON_MAP:
        game_map[x_axis][y_axis] = REPRESENTATION_MISS_ON_MAP
        print('You\'ve missed!')
        return
    if game_map[x_axis][y_axis] == REPRESENTATION_SHIP_ON_MAP:
        if ship_has_no_more_lives(game_map, x_axis, y_axis):
            mark_ship_as_dead(game_map, x_axis, y_axis)
            print('You\'ve sunk a ship!')
            return
        else:
            game_map[x_axis][y_axis] = REPRESENTATION_HIT_ON_MAP
            print('You\'ve hit a ship!')
        return
    print('You\'ve hit a previous place')
    

def display_enemy_map(game_map):
    saved_matrix = deepcopy(game_map)
    for row in saved_matrix:
        for i in range(len(row)):
            if row[i] == REPRESENTATION_MISS_ON_MAP:
                row[i] = REPRESENTATION_MISS_ON_MAP
            elif row[i] == REPRESENTATION_SHIP_ON_MAP:
                row[i] = REPRESENTATION_WATER_ON_MAP
            elif row[i] == REPRESENATATION_SUNK_ON_MAP:
                row[i] = REPRESENATATION_SUNK_ON_MAP
            elif row[i] == REPRESENTATION_HIT_ON_MAP:
                row[i] = REPRESENTATION_HIT_ON_MAP
            elif row[i] == REPRESENTATION_WATER_ON_MAP:
                row[i] = REPRESENTATION_WATER_ON_MAP
    display_game_map(saved_matrix)
 
       

def has_lost(enemy_map):
    sunk_count = []
    sunk_marks_number = sum(ships_for_player1)
    for row in enemy_map:
        for cell in row:
            if cell == REPRESENATATION_SUNK_ON_MAP:
                sunk_count.append(cell)
    if len(sunk_count) == sunk_marks_number:
        return True
    else:
        return False


def display_winner(player_turn):
    print(f'{player_turn} has won!')


def turn_is_valid(turn_input):
    if turn_input < 5 or turn_input > 50:
        print('Invalid input! (must be between 5-50)')
        return False
    else:
        return True


def ask_for_turn():
    user_input = int(input('Please enter a turn limit: '))
    if turn_is_valid(user_input):
        return user_input


def turn_printer(turn):
    print(f'Turns left: {turn}')



def main():
    print('=== First placement phase! ===')
    map1 = place_ships_on_map(ships_for_player1)
    input('=== Next player\'s placement phase! ===')
    map2 = place_ships_on_map(ships_for_player2)
    turns = ask_for_turn()
    turn_printer(turns)

    shooting_player_map = map1
    enemy_map = map2
    while True:
        player_turn = display_current_player_turn(shooting_player_map, map1)
        [x_axis, y_axis] = read_coordinates()
        shoot_at_coordinates(enemy_map, x_axis, y_axis)

        display_enemy_map(enemy_map)
        turns -= 1
        turn_printer(turns)
        
        if turns == 0:
            print('No more turns, it\'s a draw')
            return
        if has_lost(enemy_map):
            display_winner(player_turn)
            return 
        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp


if __name__ == "__main__":
    main()