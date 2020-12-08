import string

ships = [2,1]


def ask_input():
    while True:
        user_input = input('Please enter a row, a column [letter][number]: ')
        return user_input

def print_board(height, width):
    alphabet = string.ascii_uppercase
    first_row = []
    board = []
    count = 0
    first_row.append(' ')
    for i in range(1, height):
        first_row.append(i)
    for i in range(height):
        if i == 0:
            board.append(first_row)
        else:
            other_row = []
            count += 1 
            other_row.append(list(alphabet)[count-1])
            other_row.extend('0' * (width-1))
            board.append(other_row)
    return board

# print(print_board(6,6))

def printer(matrix):
    for row in matrix:
        string_row = [str(int) for int in row]
        print(' '.join(string_row))
        

def main():
    board1 = print_board(6,6)
    place_ships_on_map(board1)
    printer(board1)
    
    board2 = print_board(6,6)
    place_ships_on_map(board2)
    printer(board1)

if __name__ == "__main__":
    main()