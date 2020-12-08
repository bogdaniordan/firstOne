ships_for_player1 = [2,1]
ships_for_player2 = [2,2,3,4]


def create_map():
    return []

def coordinates_in_valid_format(coordinates):
    #verify if coordinates are in form letter and number
    return True

def coordinate_are_inside_map(coordinates):
    #verify if number is between 1 and 5 and letter letter between A-Z
    return True

def read_coordinates():
    while True:
        coordinates = input('Please enter coordinates in the form [letter][digit]: ')
        if coordinates_in_valid_format(coordinates):
            if coordinate_are_inside_map(coordinates):
                return coordinates

def place_ships_on_map(ships):
    game_map = create_map()
    for ship in ships:
        coordinates = read_coordinates()
        mark_ship_on_map(game_map, ship)
        display_game_map(game_map)
    return game_map


def main():
    map1 = place_ships_on_map(ships_for_player1)
    print('Player 2 turn to place ships on map!')
    map2 = place_ships_on_map(ships_for_player2)

if __name__ == "__main__":
    main()