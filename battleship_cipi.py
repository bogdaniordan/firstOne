import string
alphabet = string.ascii_uppercase

ships_for_player1 = [2,1]
ships_for_player2 = [2,2,3,4]
REPRESENTATION_WATER_ON_MAP = 0
REPRESENTATION_MISS_ON_MAP = 'M'
REPRESENTATION_SHIP_ON_MAP = 1
REPRESENTATION_HIT_ON_MAP = 'H'

def create_map():
    board = [[' ', '1', '2', '3', '4', '5'], ['A', '0', '0', '0', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', '0', '0', '0', '0']]
    return board
 

def coordinates_in_valid_format(coordinates):
    if list(coordinates)[0] in list(alphabet) and list(coordinates)[1].isdigit():
        return True
    else:
        print('Coordinates are not in a valid format (e.g. A2)!')

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
                print(x_axis, y_axis)
                return [x_axis, y_axis]

# read_coordinates()

def mark_ship_on_map(board, ship, x_axis, y_axis):
    board[x_axis][y_axis] = 'X'

def display_game_map(board):
    for row in board:
        print(' '.join(row), end='\n')

def place_ships_on_map(ships):
    game_map = create_map()
    for ship in ships:
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
                print('M')
            elif cell == REPRESENTATION_SHIP_ON_MAP:
                print('W') #W stands for water
            elif cell == REPRESENTATION_MISS_ON_MAP:
                print('M')

def has_won(enemy_map):
    pass

def display_winner(shooting_player_map):
    pass

def main():
    print('Player 1 turn to place ships on map!')
    map1 = place_ships_on_map(ships_for_player1)
    print('Player 2 turn to place ships on map!')
    map2 = place_ships_on_map(ships_for_player2)

    shooting_player_map = map1

    enemy_map = map2
    while True:
        display_current_player_turn(shooting_player_map, map1)
        [x_axis, y_axis] = read_coordinates()
        shoot_at_coordinates(enemy_map, x_axis, y_axis)
        display_enemy_map(enemy_map)
        if has_won(enemy_map):
            display_winner(shooting_player_map)
            return 
        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp

if __name__ == "__main__":
    main()