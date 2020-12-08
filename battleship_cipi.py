ships_for_player1 = [2,1]
ships_for_player2 = [2,2,3,4]
REPRESENTATION_WATER_ON_MAP = 0
REPRESENTATION_MISS_ON_MAP = 'M'
REPRESENTATION_SHIP_ON_MAP = 1
REPRESENTATION_HIT_ON_MAP = 'H'

def create_map():
    return []

def coordinates_in_valid_format(coordinates):
    #verify if coordinates are in form letter and number
    return True

def coordinate_are_inside_map(coordinates):
    #verify if number is between 1 and 5 and letter letter between A-Z
    return True

def transform_coordinates(coordinates):
    # transform from letter, number to number, number keeping track of the fact that counting in a list starts from 0  and not 1
    x_axis_coordinate = 1
    y_axis_coordinate = 1
    return [x_axis_coordinate, y_axis_coordinate]

def read_coordinates():
    while True:
        coordinates = input('Please enter coordinates in the form [letter][digit]: ')
        if coordinates_in_valid_format(coordinates):
            if coordinate_are_inside_map(coordinates):
                [x_axis, y_axis] = transform_coordinates(coordinates)
                return [x_axis, y_axis]

def place_ships_on_map(ships):
    game_map = create_map()
    for ship in ships:
        [x_axis, y_axis] = read_coordinates()
        mark_ship_on_map(game_map, ship)
        display_game_map(game_map)
    return game_map

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
        game_map[x_axis][y_axis] = REPRESENTATION_HIT_ON_MAP:
        print('You\'ve hit a ship!')

def main():
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