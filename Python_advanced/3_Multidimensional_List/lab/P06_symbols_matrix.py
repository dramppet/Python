rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(input())

searched_symbols = input()

is_find_symbol = False

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        col = col_idx
        asd = matrix[row_idx][col_idx]
        if matrix[row_idx][col_idx] == searched_symbols:
            print(f"{row_idx, col_idx}")
            is_find_symbol = True
            break
if not is_find_symbol:
    print(f"{rows} does not occur in the matrix")