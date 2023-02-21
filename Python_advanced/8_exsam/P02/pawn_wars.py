def find_player_position(matrix, player):
    for(row_idx, row) in enumerate(matrix):
        if player in row:
            return (row_idx, row.index(player))


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

current_player = 'w'
other_player = 'b'

current_player_position, other_player_position = find_player_position(matrix, 'w'), find_player_position(matrix, 'b')

current_delta = -1
other_delta = + 1

while True:

    (row, column) = current_player
    next_row = row + current_delta


    current_player_position, other_player_position = other_player_position, current_player_position
    current_delta, other_delta = other_delta, current_delta
    current_player, other_player = other_player, current_player
