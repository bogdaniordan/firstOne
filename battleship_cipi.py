import string
import os 

alphabet = string.ascii_uppercase

ships_for_player1 = [2,1]
ships_for_player2 = [2,1]
REPRESENTATION_WATER_ON_MAP = 0
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
    if list(coordinates)[0] in list(alphabet) and list(coordinates)[1].isdigit():
        return True
    else:
        print('Invalid input, coordinates are not in a valid format (e.g. A2)!')

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
                # print(x_axis, y_axis)
                return [x_axis, y_axis]

# read_coordinates()

def mark_ship_on_map(board, ship, x_axis, y_axis):
    board[x_axis][y_axis] = REPRESENTATION_SHIP_ON_MAP

def display_game_map(board):
    for row in board:
        print(' '.join(row), end='\n')

def place_ships_on_map(ships):
    # ships_number = len(ships)
    # print('You have {ships_number} ships.')
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

# place_ships_on_map((ships_for_player2))

def display_current_player_turn(current_player_map, player_one_map):
    if current_player_map == player_one_map:
        print('Player 1 is shooting now!')
    else:
        print('Player 2 is shooting now!')

def ship_has_no_more_lives(board, x_axis, y_axis):
    pass

def mark_ship_as_dead(board, x_axis, y_axis):
    board[x_axis][y_axis] = REPRESENATATION_SUNK_ON_MAP
    # if ship is bigger than 1 cell, it needs to mark the whole ship as dead. not only 1 cell
    if board[x_axis][y_axis + 1] == REPRESENTATION_HIT_ON_MAP:
        board[x_axis][y_axis + 1] = REPRESENATATION_SUNK_ON_MAP
    elif board[x_axis][y_axis - 1] == REPRESENTATION_HIT_ON_MAP:
        board[x_axis][y_axis - 1] = REPRESENATATION_SUNK_ON_MAP

def shoot_at_coordinates(game_map, x_axis, y_axis):
    if game_map[x_axis][y_axis] == REPRESENTATION_WATER_ON_MAP:
        game_map[x_axis][y_axis] = REPRESENTATION_MISS_ON_MAP
        print('You\'ve missed!')
        return
    if game_map[x_axis][y_axis] == REPRESENTATION_SHIP_ON_MAP:
        if ship_has_no_more_lives(game_map, x_axis, y_axis):
            mark_ship_as_dead(game_map, x_axis, y_axis)
        else:
            game_map[x_axis][y_axis] = REPRESENTATION_HIT_ON_MAP
            print('You\'ve hit a ship!')
        return
    print('You\'ve hit a previous place')
    
def display_enemy_map(game_map):
    for row in game_map:
        for cell in row:
            if cell == REPRESENTATION_MISS_ON_MAP:
                cell = REPRESENTATION_MISS_ON_MAP
            elif cell == REPRESENTATION_SHIP_ON_MAP:
                cell = REPRESENTATION_WATER_ON_MAP
            elif cell == REPRESENATATION_SUNK_ON_MAP:
                cell = REPRESENATATION_SUNK_ON_MAP
            elif cell == REPRESENTATION_HIT_ON_MAP:
                cell = REPRESENTATION_HIT_ON_MAP
            else:
                cell = REPRESENTATION_WATER_ON_MAP
    for row in game_map:
        print(' '.join(row), end='\n')

def has_won(enemy_map):
    pass

def display_winner(shooting_player_map):
    pass

def main():
    print('=== First placement phase! ===')
    map1 = place_ships_on_map(ships_for_player1)
    print('=== Next player\'s placement phase! ===')
    map2 = place_ships_on_map(ships_for_player2)
    #TREBUIE BAGATA FUNCTIE DE CLEAR TERMINAL
    shooting_player_map = map1

    enemy_map = map2
    while True:
        display_current_player_turn(shooting_player_map, map1)
        [x_axis, y_axis] = read_coordinates()
        shoot_at_coordinates(enemy_map, x_axis, y_axis)
        display_enemy_map(enemy_map)
        # display_game_map(enemy_map)
        if has_won(enemy_map):
            display_winner(shooting_player_map)
            return 
        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp

if __name__ == "__main__":
    main()