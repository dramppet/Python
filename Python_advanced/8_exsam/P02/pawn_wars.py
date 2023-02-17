def find_player_position(matrix, player):
    pass


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

current_player, other_player = find_player_position(matrix, 'w'), find_player_position(matrix, 'b')

current_delta = -1
other_delta = + 1
